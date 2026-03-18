from fastapi import FastAPI, Path, Request

app = FastAPI()

@app.get("/")
def home():
    return " Home page "

@app.get("/products")
def get_all_products():
    return "all products"