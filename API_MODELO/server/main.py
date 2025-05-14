import os
import mlflow
from dotenv import load_dotenv
from fastapi import FastAPI
from contextlib import asynccontextmanager
import routes.predictions as predictionRouter

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
    print(model)
    app.state.model = model
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

app.include_router(predictionRouter.router)