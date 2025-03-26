from fastapi import FastAPI, Depends, HTTPException
from typing import Union
from pydantic import BaseModel
from sqlmodel import Session
from models import SQLModel
from database import engine
from routers import router

app = FastAPI()

@app.on_event("startup")
def startup():
    SQLModel.metadata.create_all(engine)

@app.get("/")
def read_root():
    return {"message": "Hello1243!"}

app.include_router(router)