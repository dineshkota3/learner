# Learner - FastAPI Hello World Application

A simple FastAPI application with a hello world endpoint.

## Installation

```bash
poetry install
```

## Running the application

```bash
poetry run uvicorn main:app --reload
```

The application will be available at `http://localhost:8000`

## API Endpoint

- `GET /` - Returns {"message": "Hello World"}
- `GET /docs` - Interactive API documentation (Swagger UI)
