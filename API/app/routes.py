from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import JSONResponse
from utils import predict_with_model
from auth import Authenticate
import os
import mlflow
import subprocess

router = APIRouter()

@router.post('/predict/combat', tags=['Predictions'], dependencies=[Depends(Authenticate())])
def prediction(request: Request, input_data ):
    try:
        response_example = {
            "code": 200,
            "data": None
        }
        prediction = predict_with_model(request, input_data)
        response_example['data'] = prediction
        return JSONResponse(status_code=response_example['code'], content=response_example)

    except Exception as error:
        return JSONResponse(status_code=400, content=error)
    
@router.post('/model/load', tags=['Model'])#, dependencies=[Depends(Authenticate())])
def change_model(name: str, version: str = 'latest', request: Request = None):
    """
    Cambia dinámicamente el modelo activo usando MLflow Registry
    """
    model_uri = f"models:/{name}/{version}"
    try:
        instalar_dependencias_modelo(model_uri)
        mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI"))
        model = mlflow.pyfunc.load_model(model_uri)
        request.app.state.model = model
        return {"code": 200, "message": f"Modelo cambiado exitosamente a: {model_uri}"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"No se pudo cargar el modelo: {e}")


def instalar_dependencias_modelo(model_uri: str):
    # Obtener el archivo de entorno del modelo (Conda o pip requirements)
    env_path = mlflow.pyfunc.get_model_dependencies(model_uri)
    
    if env_path.endswith(".yaml"):
        # Si es un archivo conda, convertirlo a requirements.txt si es posible (no siempre ideal)
        raise NotImplementedError("Instalación automática desde YAML (conda) no está soportada en este flujo.")
    
    elif env_path.endswith(".txt"):
        print(f"Instalando dependencias desde: {env_path}")
        subprocess.check_call(["pip", "install", "-r", env_path])