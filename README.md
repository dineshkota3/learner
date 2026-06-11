# Learner API - FastAPI Application

A structured FastAPI application with PostgreSQL database integration.

## Features

- Layered architecture (Controllers, Services, Entities)
- PostgreSQL database with SQLAlchemy async ORM
- Alembic database migrations
- Environment-based configuration
- Health check endpoints including database connectivity

## Project Structure

```
learner/
├── src/
│   ├── api/
│   │   ├── controllers/    # API endpoints
│   │   ├── services/       # Business logic layer
│   │   └── entities/       # Database models (SQLAlchemy base)
│   ├── core/              # Configuration & settings
│   └── db/                # Database engine & session management
├── alembic/               # Database migrations
├── main.py               # Application entry point
└── .env.example          # Environment configuration template
```

## Local Development

### Prerequisites

- Python 3.12+
- PostgreSQL 18
- Poetry

### Installation

```bash
# Install dependencies
poetry install

# Copy environment template
cp .env.example .env

# Edit .env with your local database configuration
```

### Database Setup

```bash
# Start PostgreSQL 18
brew services start postgresql@18

# Create database
createdb learner

# Run migrations
poetry run alembic upgrade head
```

### Running the Application

```bash
poetry run uvicorn main:app --reload
```

The application will be available at `http://localhost:8000`

## API Endpoints

- `GET /` - Hello World endpoint
- `GET /hello` - Returns {"message": "world"}
- `GET /health` - Basic health check
- `GET /health/db` - Database connectivity check
- `GET /docs` - Interactive API documentation (Swagger UI)

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `APP_NAME` | Application name | `Learner API` |
| `DEBUG` | Debug mode | `False` |
| `DATABASE_URL` | PostgreSQL connection string | - |
| `POSTGRES_HOST` | Database host | `localhost` |
| `POSTGRES_PORT` | Database port | `5432` |
| `POSTGRES_USER` | Database user | `postgres` |
| `POSTGRES_PASSWORD` | Database password | - |
| `POSTGRES_DB` | Database name | `learner` |

## Deployment

### Render

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Set the following environment variables:
   - `DATABASE_URL`: `postgresql+asyncpg://dinesh:YOUR_PASSWORD@dpg-d8li8ht8nd3s73e5aul0-a/language_database`
   - `PYTHON_VERSION`: `3.12.11`
4. Build Command: `poetry install`
5. Start Command: `poetry run uvicorn main:app --host 0.0.0.0 --port $PORT`

Alternatively, use the provided `render.yaml` configuration file.

### Database Migrations

After deployment, run migrations:

```bash
poetry run alembic upgrade head
```

Or set up a Render worker to automatically run migrations after deploy.

## Database

This application uses PostgreSQL 18. For production deployment on Render:

- Database Name: `language_database`
- User: `dinesh`
- Host: `dpg-d8li8ht8nd3s73e5aul0-a`

Ensure the `DATABASE_URL` environment variable is set with your database password.
