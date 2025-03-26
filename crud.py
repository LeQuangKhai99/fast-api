from sqlalchemy.orm import Session
from models import Post
from schemas import PostCreate, PostUpdate

def create_post(db: Session, post: PostCreate):
    new_post = Post(title=post.title, content=post.content)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_all_posts(db: Session):
    return db.query(Post).all()

def get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()

def update_post(db: Session, post_id: int, post: PostUpdate):
    existing_post = db.query(Post).filter(Post.id == post_id).first()
    if existing_post:
        if post.title:
            existing_post.title = post.title
        if post.content:
            existing_post.content = post.content
        db.commit()
        db.refresh(existing_post)
    return existing_post

def delete_post(db: Session, post_id: int):
    existing_post = db.query(Post).filter(Post.id == post_id).first()
    if existing_post:
        db.delete(existing_post)
        db.commit()
        return True
    return False
