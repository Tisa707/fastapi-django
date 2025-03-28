from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from . import crud, schemas
from .database import SessionLocal

router = APIRouter()


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/create_user_via_url/")
def create_user_via_url(name: str = Query(...),
                        email: str = Query(...),
                        db: Session = Depends(get_db)):
    # Create a user using the URL parameters
    user = schemas.UserCreate(name=name, email=email)
    db_user = crud.create_user(db=db, user=user)
    return db_user


# Get a list of users
@router.get("/users/", response_model=list[schemas.User])
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = crud.get_users(db=db, skip=skip, limit=limit)
    return users


# Get a user by ID
@router.get("/users/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# Update a user by ID
@router.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int,
                user: schemas.UserCreate,
                db: Session = Depends(get_db)):
    db_user = crud.update_user(db=db, user_id=user_id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# Delete a user by ID
@router.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
