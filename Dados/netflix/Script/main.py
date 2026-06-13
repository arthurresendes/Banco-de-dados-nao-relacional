import uvicorn
from fastapi import FastAPI
from rotas import router

app = FastAPI(title="API-Netflix")
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)