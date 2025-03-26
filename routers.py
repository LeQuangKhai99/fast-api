from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database import get_session
import crud
from schemas import PostCreate, PostUpdate

router = APIRouter()

@router.post("/posts/")
def create(post: PostCreate, db: Session = Depends(get_session)):
    return crud.create_post(db, post)

@router.get("/posts/")
def read_all(db: Session = Depends(get_session)):
    return crud.get_all_posts(db)

@router.get("/posts/{post_id}")
def read_one(post_id: int, db: Session = Depends(get_session)):
    post = crud.get_post(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.put("/posts/{post_id}")
def update(post_id: int, post: PostUpdate, db: Session = Depends(get_session)):
    updated_post = crud.update_post(db, post_id, post)
    if not updated_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return updated_post

@router.delete("/posts/{post_id}")
def delete(post_id: int, db: Session = Depends(get_session)):
    success = crud.delete_post(db, post_id)
    if not success:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted successfully"}
