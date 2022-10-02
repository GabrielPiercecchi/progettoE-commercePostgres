from fastapi import HTTPException, status
from . import models
from . import schema


# async def new_user_register(request: schema.User, database) -> models.User:
async def new_user_register(request, database) -> models.User:
    new_user = models.User(name=request.name, email=request.email, password=request.password)
    database.add(new_user)
    database.commit()
    database.refresh(new_user)
    return new_user
