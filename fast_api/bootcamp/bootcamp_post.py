from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel, Field

class ShopInfo(BaseModel):
    name: str
    location: str

class Item(BaseModel):
    name: str = Field(min_length=4, max_length=12) # 最小文字数・最大文字数を指定
    description: Optional[str] = Field(min_length=1, max_length=100)
    price: int
    tax: Optional[float] = None

class Data(BaseModel):
    shop_info: Optional[ShopInfo] = None
    items: List[Item]

app = FastAPI()

@app.post("/")
async def create_item(data: Data):
    print("DEBUG: Call to create_item function")
    return {"data": data}
