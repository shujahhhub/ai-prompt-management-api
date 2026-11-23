from fastapi import FastAPI
from routers import prompts

app = FastAPI(
    title="AI Prompt Management API",
    description="A REST API to create, manage, search and delete AI prompts.",
    version="1.0.0"
)

# Register prompt routes
app.include_router(prompts.router)


@app.get("/")
def home():
    return {
        "message": "AI Prompt Management API is running",
        "status": "healthy"
    }