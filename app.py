from fastapi import FastAPI

from core import settings

app = FastAPI(title=settings.PROJECT_NAME)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app:app",
        port=settings.SERVER_PORT,
        host=settings.SERVER_HOST,
        reload=settings.SERVER_RELOAD,
    )
