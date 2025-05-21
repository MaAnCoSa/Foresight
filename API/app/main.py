import os
import mlflow
from dotenv import load_dotenv
from contextlib import asynccontextmanager
from routes import router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

descripcion = """
    API de Foresight.
"""

tags_metadata = [
    {
        "name": "Predictions",
        "description": "Poner texto correspondiente a la ruta"
    }
]

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    tracking_uri = os.getenv("MLFLOW_TRACKING_URI")
    if tracking_uri:
        mlflow.set_tracking_uri(tracking_uri)

    model_uri = os.getenv("MODEL_URI")
    if not model_uri:
        raise ValueError("Falta definir MODEL_URI en variables de entorno")
    
    model = mlflow.pyfunc.load_model(model_uri)
    model_name = model_uri.split("/")[1]

    app.state.model = model
    app.state.model_name = model_name

    TOKEN = os.getenv("TOKEN")
    if not TOKEN:
        raise RuntimeError("TOKEN env variable not set")
    yield

    del app.state.model

app = FastAPI(
    title="ForesightAPI",
    description=descripcion,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    openapi_tags=tags_metadata,
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],  # o especificar métodos: ["GET", "POST"]
    allow_headers=["*"],
)

app.include_router(router)