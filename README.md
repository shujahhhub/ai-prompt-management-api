# AI Prompt Management API

A RESTful API built with **Python and FastAPI** to create, retrieve, update, search, filter, and delete AI prompts.

This project demonstrates practical backend engineering concepts, including REST API development, Pydantic validation, modular architecture, API key authentication, and automated testing with Pytest.

## Features

- Create, retrieve, update, and delete prompts (CRUD).
- Search prompts by topic.
- Filter prompts by active status.
- Validate request data using Pydantic.
- Secure endpoints using API key authentication.
- Organize code using routers, schemas, services, and dependencies.
- Interactive API documentation using Swagger UI.
- Automated API tests using Pytest and FastAPI TestClient.
- Run in a reproducible Docker container.
- Run automated tests and publish a container image through GitHub Actions.

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn
- Pytest
- HTTPX
- Docker
- GitHub Actions

## Project Structure

```text
ai-prompt-management-api/
├── core/
│   ├── config.py
│   └── dependencies.py
├── routers/
│   └── prompts.py
├── schemas/
│   └── prompts.py
├── services/
│   └── prompt_service.py
├── tests/
│   └── test_prompts.py
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── main.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/ai-prompt-management-api.git
cd ai-prompt-management-api
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the API key

Set your development API key in PowerShell:

```powershell
$env:API_KEY="your-development-key"
```

Do not commit real API keys or secrets to GitHub.

### 5. Start the application

```bash
fastapi dev main.py
```

## API Documentation

Once the application is running, visit:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

Use the `x-api-key` header to authenticate protected endpoints.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Health check |
| POST | `/prompts/` | Create a prompt |
| GET | `/prompts/` | Retrieve all prompts |
| GET | `/prompts/{prompt_id}` | Retrieve one prompt |
| PUT | `/prompts/{prompt_id}` | Fully update a prompt |
| PATCH | `/prompts/{prompt_id}` | Partially update a prompt |
| DELETE | `/prompts/{prompt_id}` | Delete a prompt |
| GET | `/prompts/search?topic=Python` | Search by topic |

## Running Automated Tests

Run the complete test suite:

```bash
python -m pytest -v
```

Tests cover API responses, CRUD operations, validation, authentication, missing resources, and test isolation.

## Docker

Build the Docker image:

```bash
docker build -t ai-prompt-management-api .
```

Run the container:

```bash
docker run --rm -p 8000:8000 -e API_KEY="dev-secret-123" ai-prompt-management-api
```

The API will be available at:

- Swagger UI: http://localhost:8000/docs
- OpenAPI schema: http://localhost:8000/openapi.json

## CI/CD

The GitHub Actions workflow at [`.github/workflows/ci-cd.yml`](/.github/workflows/ci-cd.yml) runs on pushes and pull requests targeting `main`.

The workflow:

1. Checks out the repository.
2. Sets up Python 3.12.
3. Installs dependencies from `requirements.txt`.
4. Runs the complete Pytest suite.
5. Sets up Docker Buildx.
6. Publishes the Docker image to GitHub Container Registry for pushes to `main`.

The published image is:

```text
ghcr.io/shujahhhub/ai-prompt-management-api:latest
```

## Current Limitations

- Uses in-memory storage; data resets when the application restarts.
- API key authentication is a basic demonstration, not a complete production authentication system.
- No persistent database integration yet.

## Future Improvements

- Integrate SQLite or PostgreSQL for persistent storage.
- Add user-based authentication and authorization.
- Add pagination and advanced search.
- Deploy the API to a cloud platform.

## Author

Developed as a standalone AI Engineering and Backend Development portfolio project.
