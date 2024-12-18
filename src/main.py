from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
# from bson import ObjectId
# from pydantic import BaseModel
# from db import get_db
app = FastAPI(
		title="antd-pwa-server-db",
    description="FastAPI와 MongoDB를 사용한 백엔드 API 서버",
    version="0.1.0",
)

origins = [
    "http://kkushik.mooo.com:12500",
    "https://kkushik.mooo.com:12500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello, World!"}
