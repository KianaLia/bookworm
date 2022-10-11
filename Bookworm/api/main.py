from fastapi import FastAPI
import uvicorn

from data.database import *

app = FastAPI()
database = Redis()

@app.get("/")
def root():
    return 'Wlecome to the FASTAPI of Bookworm Project!\n please go to \docs to visit the Swagger API'

@app.get("/user_recoms/{user_id}")
def user_info(user_id):
    return database.load('user', user_id)

@app.get("/model_info/{model_type}/{model_id}")
def model_info(model_type, model_id):
    return database.load(model_type, model_id)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5020)