# AgriSmart Backend

FastAPI backend for AgriSmart 2.0.

## Requirements

- Python 3.12+
- PostgreSQL 16+

## Local setup

### Windows

```powershell
cd backend
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload
```

### API

- Health: GET /health
- API status: GET /api/v1/status
- Swagger: http://127.0.0.1:8000/docs
- OpenAPI: http://127.0.0.1:8000/openapi.json

## Test

```powershell
pytest
```
