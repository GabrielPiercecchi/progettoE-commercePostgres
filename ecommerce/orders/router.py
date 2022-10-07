from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import ecommerce.user.schema
from ecommerce import db
from . import services
from . import schema
from ..auth.jwt import get_current_user

router = APIRouter(
    tags=["Orders"],
    prefix='/orders'
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schema.ShowOrder)
async def initiate_order_processing(user_email, database: Session = Depends(db.get_db),
                                    current_user: ecommerce.user.schema.User = Depends(get_current_user)):
    result = await services.initiate_order(user_email, database)
    return result


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schema.ShowOrder])
async def orders_list(user_email: str, database: Session = Depends(db.get_db)):
    result = await services.get_order_listing(user_email, database)
    return result
