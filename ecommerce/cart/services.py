from typing import List

from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session

import ecommerce
from ecommerce import db
from ecommerce.products.models import Product
from ecommerce.user.models import User
from .models import Cart, CartItems
from . import schema, models
from .schema import ShowCart


async def add_items(cart_id, product_id, database: Session = Depends(db.get_db)):
    cart_items = CartItems(cart_id=cart_id, product_id=product_id)
    database.add(cart_items)
    database.commit()
    database.refresh(cart_items)


async def add_to_cart_by_id(product_id, user_id, database: Session = Depends(db.get_db)):
    user_info = database.query(ecommerce.user.models.User).get(user_id)
    product_info = database.query(Product).get(product_id)
    cart_info = database.query(Cart).filter(Cart.user_id == user_info.id).first()

    if not user_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found !")
    if not product_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product Not Found !")
    if product_info.quantity <= 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Items Out of Stock !")

    if not cart_info:
        new_cart = Cart(user_id=user_info.id)
        database.add(new_cart)
        database.commit()
        database.refresh(new_cart)
        await add_items(new_cart.id, product_info.id, database)
    else:
        await add_items(cart_info.id, product_info.id, database)
    return {"status": "Item Added to Cart"}


# async def add_to_cart(product_id, database: Session = Depends(db.get_db)):
#     product_info = database.query(Product).get(product_id)
#     if not product_id:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data Not Found !")
#
#     if product_info.quantity <= 0:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Items Out of Stock !")
#
#     user_info = database.query(User).filter(User.email == "elon@tesla.com").first()
#
#     cart_info = database.query(Cart).filter(Cart.user_id == user_info.id).first()
#
#     if not cart_info:
#         new_cart = Cart(user_id=user_info.id)
#         database.add(new_cart)
#         database.commit()
#         database.refresh(new_cart)
#         await add_items(new_cart.id, product_info.id, database)
#     else:
#         await add_items(cart_info.id, product_info.id, database)
#     return {"status": "Item Added to Cart"}


# async def get_all_items(database) -> ShowCart:
#     user_info = database.query(User).filter(User.email == "elon@tesla.com").first()
#     cart = database.query(Cart).filter(Cart.user_id == user_info.id).first()
#     return cart


async def get_all_items_id(user_id, database) -> ShowCart:
    user_info = database.query(ecommerce.user.models.User).get(user_id)
    if not user_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data Not Found !")
    cart = database.query(Cart).filter(Cart.user_id == user_info.id).first()
    return cart


# async def remove_cart_item(cart_item_id, database) -> None:
#     user_info = database.query(User).filter(User.email == "elon@tesla.com").first()
#     cart_id = database.query(Cart).filter(User.id == user_info.id).first()
#     database.query(CartItems).filter(CartItems.id == cart_item_id,
#                                      CartItems.cart_id == cart_id.id).delete()
#     database.commit()
#     return


async def remove_cart_item_email(cart_item_id, database) -> None:
    # user_info = database.query(User).filter(User.email == user_email).first()
    # cart_id = database.query(Cart).filter(User.id == user_info.id).first()

    database.query(CartItems).filter(CartItems.id == cart_item_id).delete()
    database.commit()
    return
