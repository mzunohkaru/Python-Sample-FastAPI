from fastapi import FastAPI
from os import environ as env

app = FastAPI()

@app.get("/")
def read_root():
    return {"Message": f"secret: {env['MY_VARIABLE']}"}

