from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello PyCharm "}


@app.get("/hello/{name}")
async def say_hello(name: int):
    return {"message": f"Hello {name}"}
