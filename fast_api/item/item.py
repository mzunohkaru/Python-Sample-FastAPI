from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: int
    brand: Optional[str] = None


class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[int] = None
    brand: Optional[str] = None


inventory = {
    1: {
        "name": "Meat",
        "price": 460,
        "brand": "Regular",
    },
    2: {
        "name": "Ege",
        "price": 290,
        "brand": "Premium",
    },
}


@app.get("/get-all-item")
async def get_all_item():
    return inventory


@app.get("/get-item/{item_id}")
async def get_item(
    item_id: int = Path(
        None, description="The ID of the item you'd like to view.", gt=0
    )
):
    return inventory[item_id]


@app.post("/create-item/{item_id}")
async def create_item(item_id: int, item: Item):
    if item_id in inventory:
        raise HTTPException(status_code=400, detail="Item ID already exists.")

    inventory[item_id] = item
    return inventory[item_id]


@app.put("/update-item/{item_id}")
async def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item ID dose not already exist.")

    if item.name != None:
        inventory[item_id].name = item.name

    if item.price != None:
        inventory[item_id].price = item.price

    if item.brand != None:
        inventory[item_id].brand = item.brand
    else :
        inventory[item_id].brand = None

    return inventory[item_id]


@app.delete("/delete-item")
async def delete_item(
    item_id: int = Query(..., description="The ID of the item to delete", gt=0)
):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="ID does not exist.")

    del inventory[item_id]
    return {"Success": "Item deleted"}
