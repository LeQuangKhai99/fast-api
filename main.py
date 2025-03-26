from fastapi import FastAPI, Depends, HTTPException
from typing import Union
from pydantic import BaseModel
from sqlmodel import Session

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello1243!"}