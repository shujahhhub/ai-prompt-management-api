
from pydantic import BaseModel, Field


class PromptCreate(BaseModel):
    topic: str = Field(
        min_length=2,
        max_length=50
    )
    prompt: str = Field(
        min_length=5,
        max_length=1000
    )
    active: bool = True


class PromptUpdate(BaseModel):
    topic: str = Field(
        min_length=2,
        max_length=50
    )
    prompt: str = Field(
        min_length=5,
        max_length=1000
    )
    active: bool


class PromptPatch(BaseModel):
    topic: str | None = Field(
        default=None,
        min_length=2,
        max_length=50
    )
    prompt: str | None = Field(
        default=None,
        min_length=5,
        max_length=1000
    )
    active: bool | None = None


class PromptResponse(BaseModel):
    id: int
    topic: str
    prompt: str
    active: bool
