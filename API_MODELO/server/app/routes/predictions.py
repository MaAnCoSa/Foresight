from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
# from models.combat_input import CombatInput
from modules.predict import predict_with_model

router = APIRouter(
    prefix=("/predict"),
    tags=["Predicts"]
)

@router.post('/combat')
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

@router.get('/prueba')
def prediction( ):
    try:
        response_example = {
            "code": 200,
            "data": "Se logro hacer la peticion"
        }
        return JSONResponse(status_code=response_example['code'], content=response_example)

    except Exception as error:
        return JSONResponse(status_code=400, content=error)