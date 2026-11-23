from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader

from core.config import API_KEY

api_key_header = APIKeyHeader(
    name="x-api-key",
    auto_error=False
)


def verify_api_key(
    x_api_key: str | None = Security(api_key_header)
):
    if not API_KEY or x_api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key"
        )

    return True