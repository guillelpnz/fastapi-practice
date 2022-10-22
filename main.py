from fastapi import FastAPI
from enum import Enum


class ModelName(str, Enum):
    pepe = "pepe"
    rere = "rere"
    lele = "lele"

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/models/{model_name}")
def get_model(model_name: ModelName):
    response = {"model_name": model_name}
    if model_name is ModelName.pepe:
        return {**response, "message": "Pepe FTW!"}
    elif model_name.value == "rere":
        return {**response, "message": "Rere FTW!"}

    return {**response, "message": "Lele FTW!"}
