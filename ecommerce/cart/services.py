from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session

from ecommerce import db
from ecommerce.products.models import Product
from ecommerce.user.models import User
from . models import Cart, CartItems


async def add_to_cart(product_id, database: Session = Depends(db.get_db)):
    product_info = database.query(Product).get(product_id)
    if not product_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data Not Found !")

    if product_info <= 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Items Out of Stock !")

    user_info = database.query(User).filter(User.email == "elon@tesla.com").first()

    cart_info = database.query(Cart).filter(Cart.user_id == user_info.id).first()

    if not cart_info:
        new_cart = Cart(user_id=user_info.id)
        database.add(new_cart)
        database.commit()
        database.refresh(new_cart)
        await add_items(new_cart.id, database) #min 18:52
