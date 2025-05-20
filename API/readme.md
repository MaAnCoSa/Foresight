# Foresight API
<a href="https://cookiecutter-data-science.drivendata.org/" target="_blank">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>
<a href="https://github.com/MaAnCoSa/Foresight" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-hosted-181717?logo=github" />
</a>

This API uses FastAPI to serve Machine Learning models registered in MLflow and hosted at [DagsHub](https://dagshub.com/).

---

## Project structure
```text
.
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── auth.py
│   └── utils.py
├── .env
├── requirements.txt
├── Dockerfile
├── docker-composer.yml
└── README.md
```

---

## Manual Installation
### 1. Creates virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Define environment variables
Create an `.env` file with the following variables:
```env
MLFLOW_TRACKING_URI=https://dagshub.com/<usuario>/<repo>.mlflow
MODEL_URI=models:/Champeon/1
TOKEN=tu_api_key_segura
```
| Nombre               | Descripción                                                       |
|----------------------|-------------------------------------------------------------------|
| `MLFLOW_TRACKING_URI`| MLflow server URL (e.g., DagsHub's)                               |
| `MODEL_URI`          | URI of the registered model (e.g. `models:/Champeon/1`)           |
| `TOKEN`              | Token used to authenticate requests to the API                    |

### 4. Deployment
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Security
To protect the routes, a header with your API token is required:
```http
x-api-key: mi_api_token_seguro
```
> *NOTE: The use of a fixed token from environment variables is a simple solution for testing or controlled environments. It is not recommended for production use. In a real environment, you should implement more robust authentication, such as OAuth2, JWT, or a solution with users and roles. Here it is used only to limit access to a few users.

## Deployment with Docker
### 1. Build the image
```bash
docker build -t api .
```
### 2. Execute container
```bash
docker run -p 8000:8000 api
```
> This will run the API inn `http://localhost:8000`.

## Deployment with Docker Compose
### 1. Building  y Run services
```bash
docker compose up --build
```
### 2. Stop services
```bash
docker compose down
```
> This will run the API in `http://localhost:8000`.