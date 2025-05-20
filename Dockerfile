# Imagen de Python
FROM python:3.12-slim

# Directorio del proyecto
WORKDIR /app

# Copiar archivos
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app/* ./

# Abrir puerto
EXPOSE 8000

# Comando para ejecutar la app
CMD ["uvicorn", "main:app", "--reload","--host", "0.0.0.0", "--port", "8000"]