from fastapi import FastAPI
from api import router
from core import settings

app = FastAPI(title=settings.PROJECT_NAME)
app.include_router(router=router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app:app",
        port=settings.SERVER_PORT,
        host=settings.SERVER_HOST,
        reload=settings.SERVER_RELOAD,
    )
