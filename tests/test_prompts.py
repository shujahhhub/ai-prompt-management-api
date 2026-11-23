from fastapi.testclient import TestClient
from main import app
import pytest
from services import prompt_service

@pytest.fixture(autouse=True)
def reset_prompts():
    prompt_service.prompts.clear()

    prompt_service.prompts.extend([
        {
            "id": 1,
            "topic": "Python",
            "prompt": "Explain Python fundamentals",
            "active": True
        },
        {
            "id": 2,
            "topic": "RAG",
            "prompt": "Explain retrieval augmented generation",
            "active": True
        },
        {
            "id": 3,
            "topic": "AI Agents",
            "prompt": "Explain AI agents",
            "active": False
        }
    ])

    prompt_service.next_prompt_id = 4

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_get_prompts():
    response = client.get(
        "/prompts/",
        headers={"x-api-key": "dev-secret-123"}
    )

    assert response.status_code == 200


def test_create_prompt():
    response = client.post(
        "/prompts/",
        headers={"x-api-key": "dev-secret-123"},
        json={
            "topic": "Testing",
            "prompt": "Explain automated API testing",
            "active": True
        }
    )

    assert response.status_code == 201
    assert response.json()["topic"] == "Testing"


def test_invalid_prompt():
    response = client.post(
        "/prompts/",
        headers={"x-api-key": "dev-secret-123"},
        json={
            "topic": "A",
            "prompt": "Invalid topic",
            "active": True
        }
    )

    assert response.status_code == 422


def test_missing_api_key():
    response = client.get("/prompts/")

    assert response.status_code == 401


def test_update_prompt():
    headers = {"x-api-key": "dev-secret-123"}

    created = client.post(
        "/prompts/",
        headers=headers,
        json={
            "topic": "Original",
            "prompt": "Original prompt text",
            "active": True
        }
    )

    prompt_id = created.json()["id"]

    response = client.put(
        f"/prompts/{prompt_id}",
        headers=headers,
        json={
            "topic": "Updated",
            "prompt": "Updated prompt text",
            "active": False
        }
    )

    assert response.status_code == 200
    assert response.json()["topic"] == "Updated"
    assert response.json()["active"] is False


def test_patch_prompt():
    headers = {"x-api-key": "dev-secret-123"}

    created = client.post(
        "/prompts/",
        headers=headers,
        json={
            "topic": "Python",
            "prompt": "Learn Python programming",
            "active": True
        }
    )

    prompt_id = created.json()["id"]

    response = client.patch(
        f"/prompts/{prompt_id}",
        headers=headers,
        json={"active": False}
    )

    assert response.status_code == 200
    assert response.json()["active"] is False
    assert response.json()["topic"] == "Python"


def test_delete_prompt():
    headers = {"x-api-key": "dev-secret-123"}

    created = client.post(
        "/prompts/",
        headers=headers,
        json={
            "topic": "Delete Test",
            "prompt": "Test prompt deletion",
            "active": True
        }
    )

    prompt_id = created.json()["id"]

    response = client.delete(
        f"/prompts/{prompt_id}",
        headers=headers
    )

    assert response.status_code == 200

    check = client.get(
        f"/prompts/{prompt_id}",
        headers=headers
    )

    assert check.status_code == 404


def test_update_missing_prompt():
    response = client.put(
        "/prompts/99999",
        headers={"x-api-key": "dev-secret-123"},
        json={
            "topic": "Python",
            "prompt": "Learn Python",
            "active": True
        }
    )

    assert response.status_code == 404