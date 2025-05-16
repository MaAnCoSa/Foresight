import os
import mlflow
import logging
from dotenv import load_dotenv
from contextlib import asynccontextmanager
import routes.predictions as predictionRouter
from fastapi import FastAPI, Request, HTTPException

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
    app.state.model = model

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

@app.middleware("http")
async def require_api_key(request: Request, call_next):
    try:
        if request.headers.get("x-api-key") != os.getenv("TOKEN"):
            raise HTTPException(status_code=403, detail="No autorizado")
        return await call_next(request)
    except HTTPException as e:
        from fastapi.responses import JSONResponse
        return JSONResponse(
            status_code=e.status_code,
            content={"detail": e.detail}
        )

app.include_router(predictionRouter.router)