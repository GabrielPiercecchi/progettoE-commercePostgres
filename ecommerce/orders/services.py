from typing import List

from fastapi import HTTPException, status

from ecommerce.cart.models import Cart, CartItems
from ecommerce.orders.models import Order, OrderDetails
from ecommerce.user.models import User


async def initiate_order(user_email, database) -> Order:
    user_info = database.query(User).filter(User.email == user_email).first()
    cart = database.query(Cart).filter(Cart.user_id == user_info.id).first()

    cart_items_objects = database.query(CartItems).filter(Cart.id == cart.id)
    if not cart_items_objects.count():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Items Found in Cart !")

    total_amount: float = 0.0
    for item in cart_items_objects:
        total_amount += item.products.price

    new_order = Order(order_amount=total_amount,
                      customer_id=user_info.id,
                      shipping_address="Via Osimo 3, Roma, Italia")
    database.add(new_order)
    database.commit()
    database.refresh(new_order)

    bulk_order_details_objects = list()

    for item in cart_items_objects:
        new_order_details = OrderDetails(order_id=new_order.id,
                                         product_id=item.products.id)
        bulk_order_details_objects.append(new_order_details)

    database.bulk_save_objects(bulk_order_details_objects)
    database.commit()

    # Send Email

    # Clear items in the cart
    database.query(CartItems).filter(CartItems.cart_id == cart.id).delete()
    database.commit()

    return new_order


async def get_order_listing(user_email, database) -> List[Order]:
    user_info = database.query(User).filter(User.email == user_email).first()
    orders = database.query(Order).filter(Order.customer_id == user_info.id).all()
    return orders
