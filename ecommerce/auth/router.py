from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .jwt import create_access_token
from ecommerce import db
from ecommerce.user import hashing
from ecommerce.user.models import User

router = APIRouter(tags=["Auth"])


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), database: Session = Depends(db.get_db)):
    user = database.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials !")
    if not database.query(User).filter(request.password == user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid password !")

    # Generate a JWT Token
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
