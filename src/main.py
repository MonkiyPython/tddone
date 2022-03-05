from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"Hello": "From Rajath Home"}
