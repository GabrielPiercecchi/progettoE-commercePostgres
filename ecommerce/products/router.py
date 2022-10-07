from typing import List

from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session

import ecommerce.user.schema
from ecommerce import db
from . import schema
from . import services
from . import validator
from ..auth.jwt import get_current_user

router = APIRouter(
    tags=['Products'],
    prefix='/products'
)


@router.post('/category', status_code=status.HTTP_201_CREATED)
async def create_category(request: schema.Category, database: Session = Depends(db.get_db),
                          current_user: ecommerce.user.schema.User = Depends(get_current_user)):
    new_category = await services.create_new_category(request, database)
    return new_category


@router.get('/category', response_model=List[schema.ListCategory])
async def get_all_categories(database: Session = Depends(db.get_db)):
    return await services.get_all_categories(database)


@router.get('/category/{category_id}', response_model=schema.ListCategory)
async def category_by_id(category_id: int, database: Session = Depends(db.get_db)):
    return await services.get_category_by_id(category_id, database)


@router.delete('/category/{category_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_category_by_id(category_id: int, database: Session = Depends(db.get_db),
                                current_user: ecommerce.user.schema.User = Depends(get_current_user)):
    return await services.delete_category_by_id(category_id, database)


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_product(request: schema.Product, database: Session = Depends(db.get_db),
                         current_user: ecommerce.user.schema.User = Depends(get_current_user)):
    category = await validator.verify_category_exists(request.category_id, database)
    if not category:
        raise HTTPException(
            status_code=400,
            detail="You have provided invalid category id"
        )
    product = await services.create_new_product(request, database)
    return product


@router.get('/', response_model=List[schema.ProductListing])
async def get_all_products(database: Session = Depends(db.get_db)):
    return await services.get_all_products(database)


@router.delete('/{product_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_products_by_id(product_id: int, database: Session = Depends(db.get_db),
                                current_user: ecommerce.user.schema.User = Depends(get_current_user)):
    return await services.delete_products_by_id(product_id, database)
