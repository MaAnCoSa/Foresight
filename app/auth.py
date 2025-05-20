from fastapi import Request, HTTPException
import os

class Authenticate:
    def __call__(self, request: Request):
        token = request.headers.get("x-api-key")
        if token != os.getenv("TOKEN"):
            raise HTTPException(
                status_code=403,
                detail='No autorizado'
            )