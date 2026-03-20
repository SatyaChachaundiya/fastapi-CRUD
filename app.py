from fastapi import FastAPI, Path, Request
from models import Product
app = FastAPI()

products = [
    Product(id=1,name="phone",description="budget phone",price=98,quantity=10),
    Product(id=2,name="laptop",description="gaming laptop",price=98,quantity=10)
]

@app.get("/")
def home():
    return " Home page "

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return "product not found"

@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product

@app.put("/product")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "product updated"
    return "product not found"

@app.delete("/product")
def delete_product_by_id(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return " product deleted"
    return "product not found"
    
