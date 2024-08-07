from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal, engine, Base
from app.models import Product
from app.crud import get_products, get_product_by_id, create_product, update_product, delete_product
from app.schemas import ProductCreate, ProductResponse

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependencia para obtener la sesión de la base de datos


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/v2/products", response_model=List[ProductResponse])
async def read_products(db: Session = Depends(get_db)):
    return get_products(db)


@app.get("/api/v2/products/{product_id}", response_model=ProductResponse)
async def read_product(product_id: str, db: Session = Depends(get_db)):
    product = get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.post("/api/v2/products", response_model=ProductResponse, status_code=201)
async def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)


@app.patch("/api/v2/products/{product_id}", response_model=ProductResponse)
async def update_product(product_id: str, updated_product: ProductCreate, db: Session = Depends(get_db)):
    product = get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return update_product(db, product, updated_product)


@app.delete("/api/v2/products/{product_id}", response_model=ProductResponse)
async def delete_product(product_id: str, db: Session = Depends(get_db)):
    product = get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return delete_product(db, product)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="141.148.55.107", port=9101)
