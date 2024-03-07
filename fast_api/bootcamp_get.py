from typing import Optional
from fastapi import FastAPI

app = FastAPI()

# パスパラメーター
@app.get("/user/{name}")
async def user(name: str):
    print("DEBUG: Call to user function")
    return {"User Name": name}

# http://127.0.0.1:8000/user/naoki
# 結果 : {"User Name":"naoki"}


# クエリパラメーター
@app.get("/items/")
async def items(item_name: str = 'Japan', item_no: int = '2'):
    return {"Item Name": item_name, "Item No": item_no}

# http://127.0.0.1:8000/items/
# 結果 : {"Item Name":"Japan","Item No":"2"}

# http://127.0.0.1:8000/items/?item_name=America&item_no=1
# 結果 : {"Item Name":"America","Item No":1}f


# パスパラメーター & クエリパラメーター
@app.get("/country/{country_name}")
async def search(country_name: str, city_name: str = '---'):
    return {"Search Query": country_name, "Search Result": f"{country_name},{city_name}"}

# http://127.0.0.1:8000/country/japan
# 結果 : {"Search Query":"japan","Search Result":"japan,---"}
# http://127.0.0.1:8000/country/japan?city_name=tokyo
# 結果 : {"Search Query":"japan","Search Result":"japan,tokyo"}


# オプションパラメーター
# Optional: パラメーターが必須ではないことを示す
@app.get("/products/")
async def products(product_id: int, product_name: Optional[str] = None):
    return {"Product ID": product_id, "Product Name": product_name}

# http://127.0.0.1:8000/products/?product_id=20
# 結果 : {"Product ID":20,"Product Name":null}