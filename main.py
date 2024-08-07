from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uuid
import uvicorn

app = FastAPI()

# Modelo de datos para el producto


class Product(BaseModel):
    id: Optional[str] = None
    name: str
    price: float
    stock: int
    urlImage: str
    description: str
    v: int


# Simulación de una base de datos en memoria
products_db = []


@app.get("/api/v2/products", response_model=List[Product])
async def get_products():
    return products_db


@app.get("/api/v2/products/{product_id}", response_model=Product)
async def get_product_by_id(product_id: str):
    for product in products_db:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")


@app.post("/api/v2/products", response_model=Product, status_code=201)
async def create_product(product: Product):
    product.id = str(uuid.uuid4())
    products_db.append(product)
    return product


@app.patch("/api/v2/products/{product_id}", response_model=Product)
async def update_product(product_id: str, updated_product: Product):
    for index, product in enumerate(products_db):
        if product.id == product_id:
            updated_product.id = product_id  # Ensure the ID remains the same
            products_db[index] = updated_product
            return updated_product
    raise HTTPException(status_code=404, detail="Product not found")


@app.delete("/api/v2/products/{product_id}", response_model=Product)
async def delete_product(product_id: str):
    for index, product in enumerate(products_db):
        if product.id == product_id:
            deleted_product = products_db.pop(index)
            return deleted_product
    raise HTTPException(status_code=404, detail="Product not found")

if __name__ == "__main__":
    uvicorn.run(app, host="141.148.55.107", port=9101)
