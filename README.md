# AI Prompt Management API

A RESTful API built with **Python and FastAPI** to create, retrieve, update, search, filter, and delete AI prompts.

This project demonstrates backend engineering and DevOps practices, including REST API development, Pydantic validation, API key authentication, automated testing, Docker containerization, and CI/CD with GitHub Actions.

## Features

- Complete CRUD operations for AI prompts.
- Search prompts by topic.
- Filter prompts by active status.
- Request validation using Pydantic.
- API key authentication.
- Modular application architecture.
- Interactive Swagger API documentation.
- Automated API testing using Pytest.
- Docker containerization.
- Automated CI/CD pipeline using GitHub Actions.
- Docker image publishing to GitHub Container Registry (GHCR).

## Tech Stack

| Category | Technologies |
|---|---|
| Language | Python 3.12 |
| Backend | FastAPI |
| Validation | Pydantic |
| Server | Uvicorn |
| API Testing | Pytest, HTTPX |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Container Registry | GitHub Container Registry (GHCR) |
| Version Control | Git, GitHub |

## Project Architecture

```text
ai-prompt-management-api/
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── core/
│   ├── config.py
│   └── dependencies.py
│
├── routers/
│   └── prompts.py
│
├── schemas/
│   └── prompt.py
│
├── services/
│   └── prompt_service.py
│
├── tests/
│   └── test_prompts.py
│
├── main.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

## Installation and Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/shujahhhub/ai-prompt-management-api.git
cd ai-prompt-management-api
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the API key

Set an environment variable in PowerShell:

```powershell
$env:API_KEY="your-development-key"
```

Never commit real API keys or secrets to GitHub.

### 5. Start the application

```bash
fastapi dev main.py
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI provides interactive API documentation through Swagger UI.

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
- OpenAPI Specification: http://127.0.0.1:8000/openapi.json

Protected endpoints require the `x-api-key` header.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API health check |
| POST | `/prompts/` | Create a prompt |
| GET | `/prompts/` | Retrieve all prompts |
| GET | `/prompts/{prompt_id}` | Retrieve a specific prompt |
| PUT | `/prompts/{prompt_id}` | Fully update a prompt |
| PATCH | `/prompts/{prompt_id}` | Partially update a prompt |
| DELETE | `/prompts/{prompt_id}` | Delete a prompt |
| GET | `/prompts/search?topic=Python` | Search prompts by topic |

## Docker

The application is containerized using Docker, allowing it to run in an isolated environment with its required dependencies.

### Build the Docker image

```bash
docker build -t ai-prompt-management-api .
```

### Run the container

```bash
docker run -d -p 8000:8000 -e API_KEY=your-development-key --name prompt-api ai-prompt-management-api
```

### Verify the running container

```bash
docker ps
```

### View container logs

```bash
docker logs prompt-api
```

### Stop the container

```bash
docker stop prompt-api
```

### Remove the container

```bash
docker rm prompt-api
```

After starting the container, access the API documentation at:

http://127.0.0.1:8000/docs

## Automated Testing

The project uses Pytest and FastAPI TestClient to automate API testing.

Run the complete test suite:

```bash
python -m pytest -v
```

Test coverage includes:

- Health-check endpoint.
- Prompt retrieval and creation.
- PUT and PATCH operations.
- Prompt deletion.
- Invalid input validation.
- Authentication checks.
- Missing resource handling.
- Test isolation.

## CI/CD — GitHub Actions

The project includes an automated workflow configured in:

```text
.github/workflows/ci-cd.yml
```

The pipeline runs when code is pushed to the `main` branch or when a pull request targets `main`.

### Pipeline workflow

1. Checkout the GitHub repository.
2. Set up Python 3.12.
3. Install project dependencies.
4. Execute automated tests using Pytest.
5. Set up Docker Buildx.
6. Build the Docker image.
7. Publish the image to GitHub Container Registry on pushes to `main`.

### CI/CD Workflow

```text
Developer
    |
    v
Git Push / Pull Request
    |
    v
GitHub Actions
    |
    v
Checkout Repository
    |
    v
Install Dependencies
    |
    v
Run Pytest
    |
    v
Build Docker Image
    |
    v
Publish Image to GHCR
    |
    v
Successful Workflow
```

### Container Registry

Docker images are published to GitHub Container Registry.

Image location:

```text
ghcr.io/shujahhhub/ai-prompt-management-api:latest
```

Pull the image using:

```bash
docker pull ghcr.io/shujahhhub/ai-prompt-management-api:latest
```

Run the published image:

```bash
docker run -d -p 8000:8000 -e API_KEY=your-development-key --name prompt-api ghcr.io/shujahhhub/ai-prompt-management-api:latest
```

Note: The GHCR package must be publicly accessible for anonymous pulls. Private packages require authentication.

## Current Limitations

- Uses in-memory storage; data resets when the application restarts.
- API key authentication is a basic implementation, not a complete production authentication system.
- No persistent database integration.
- CI/CD publishes a Docker image but does not deploy the application to a live production server.

## Future Improvements

- Integrate PostgreSQL or SQLite for persistent storage.
- Implement stronger authentication and authorization.
- Add pagination and advanced search.
- Add Docker Compose.
- Introduce cloud deployment using AWS.
- Implement automated deployment to a cloud environment.
- Add application monitoring and logging.

## Learning Outcomes

Through this project, I gained practical experience with:

- Designing and developing REST APIs using FastAPI.
- Structuring backend applications using modular architecture.
- Implementing CRUD operations and request validation.
- Protecting endpoints using API key authentication.
- Writing automated tests using Pytest.
- Containerizing Python applications using Docker.
- Understanding Docker images, containers, ports, and environment variables.
- Creating CI/CD workflows using GitHub Actions.
- Publishing container images to GitHub Container Registry.

## Author

**Shujah Ur Rehman**

AI Engineering | Backend Development | DevOps & Cloud Engineering