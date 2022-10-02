from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from ecommerce import db
from . import schema
from . import services
from . import validator

router = APIRouter(tags=['User'], prefix='/user')


async def create_user_registration(request: schema.User, database: Session = Depends(db.get_db)):
    user = await validator.verify_email_exist(request.email, database)

    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system."
        )

        new_user = await services.new_user_register(request, database)
        return new_user

