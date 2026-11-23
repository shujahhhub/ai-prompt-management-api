
from fastapi import APIRouter, HTTPException, status, Depends
from core.dependencies import verify_api_key

from schemas.prompts import (
    PromptCreate,
    PromptUpdate,
    PromptPatch,
    PromptResponse
)

from services import prompt_service


router = APIRouter(
    prefix="/prompts",
    tags=["Prompts"],
    dependencies=[Depends(verify_api_key)]
)

@router.get("/", response_model=list[PromptResponse])
def get_prompts(active: bool | None = None):
    return prompt_service.get_all_prompts(active)


@router.get("/search", response_model=list[PromptResponse])
def search_prompts(topic: str):
    results = prompt_service.search_prompts(topic)

    if not results:
        raise HTTPException(404, "No matching prompts found")

    return results


@router.get("/{prompt_id}", response_model=PromptResponse)
def get_prompt(prompt_id: int):
    prompt = prompt_service.find_prompt(prompt_id)

    if prompt is None:
        raise HTTPException(
            status_code=404,
            detail="Prompt not found"
        )

    return prompt


@router.post(
    "/",
    response_model=PromptResponse,
    status_code=status.HTTP_201_CREATED
)
def create_prompt(prompt: PromptCreate):
    return prompt_service.create_prompt(prompt)


@router.put("/{prompt_id}", response_model=PromptResponse)
def update_prompt(prompt_id: int, prompt: PromptUpdate):
    updated = prompt_service.update_prompt(prompt_id, prompt)

    if updated is None:
        raise HTTPException(404, "Prompt not found")

    return updated


@router.patch("/{prompt_id}", response_model=PromptResponse)
def patch_prompt(prompt_id: int, prompt: PromptPatch):
    updated = prompt_service.patch_prompt(prompt_id, prompt)

    if updated is None:
        raise HTTPException(404, "Prompt not found")

    return updated


@router.delete("/{prompt_id}")
def delete_prompt(prompt_id: int):
    deleted = prompt_service.delete_prompt(prompt_id)

    if deleted is None:
        raise HTTPException(404, "Prompt not found")

    return {
        "message": "Prompt deleted successfully",
        "deleted_prompt": deleted
    }
