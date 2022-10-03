from fastapi import FastAPI
from ecommerce.user import router as user_router
from ecommerce.products import router as product_router


app = FastAPI(title="EcommerceApp",
              version="0.0.1")

app.include_router(user_router.router)
app.include_router(product_router.router)

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
