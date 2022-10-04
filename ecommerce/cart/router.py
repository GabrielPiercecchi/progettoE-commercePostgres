import decimal

from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session

import ecommerce.user.schema

from ecommerce import db
from ecommerce.user.schema import User
from . import services
from . import schema
from ..auth.jwt import get_current_user

router = APIRouter(
    tags=["Cart"],
    prefix='/cart'
)


@router.post('/add', status_code=status.HTTP_201_CREATED)
async def add_product_to_cart(product_id: int, user_id: int, database: Session = Depends(db.get_db),
                              current_user: ecommerce.user.schema.User = Depends(get_current_user)):
    result = await services.add_to_cart_by_id(product_id, user_id, database)
    return result


# @router.post('/add', status_code=status.HTTP_201_CREATED)
# async def add_product_to_cart(product_id: int, database: Session = Depends(db.get_db)):
#     result = await services.add_to_cart(product_id, database)
#     return result


# @router.get('/', response_model=schema.ShowCart)
# async def get_all_cart_items(database: Session = Depends(db.get_db)):
#     result = await services.get_all_items(database)
#     return result


@router.get('/', response_model=schema.ShowCart)
async def get_all_cart_items_by_id(user_id: int, database: Session = Depends(db.get_db),
                                   current_user: ecommerce.user.schema.User = Depends(get_current_user)):
    result = await services.get_all_items_id(user_id, database)
    return result


# @router.delete('/{cart_item_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
# async def remove_cart_item_by_id(cart_item_id: int, database: Session = Depends(db.get_db)):
#     await services.remove_cart_item(cart_item_id, database)


@router.delete('/{cart_item_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def remove_cart_item_by_id(cart_item_id: int, database: Session = Depends(db.get_db),
                                 current_user: ecommerce.user.schema.User = Depends(get_current_user)):
    await services.remove_cart_id(cart_item_id, database)
