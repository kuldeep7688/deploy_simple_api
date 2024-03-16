from fastapi import FastAPI
from os import environ as env

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World == {}!!! 33".format(env['MY_VARIABLE'])}