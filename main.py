from fastapi import FastAPI

from ecommerce.auth import router as auth_router
from ecommerce.cart import router as cart_router
from ecommerce.orders import router as order_router
from ecommerce.products import router as product_router
from ecommerce.user import router as user_router

app = FastAPI(title="EcommerceApp",
              version="0.0.1", redoc_url=None)

app.include_router(auth_router.router)
app.include_router(user_router.router)
app.include_router(product_router.router)
app.include_router(cart_router.router)
app.include_router(order_router.router)

#Test

# app = FastAPI()
#
#
# @app.get("/")
# async def root():
#     return {"message": "Hello PyCharm "}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: int):
#     return {"message": f"Hello {name}"}
