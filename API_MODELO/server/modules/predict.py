import numpy as np
from fastapi import Request

def predict_with_model(request: Request, input_data):
    model = request.app.state.model
    X = np.array([[input_data]])

    prediction = model.predict(X)
    return { "prediccion": prediction }