from pydantic import BaseModel
import numpy as np
from fastapi import Request

class CombatInput (BaseModel):
    feature1: float
    feature2: float
    feature3: float

def predict_with_model(request: Request, input_data):
    model = request.app.state.model
    X = np.array([[input_data]])
    prediction = model.predict(X)

    return { "prediccion": prediction }