from sqlalchemy.orm import Session
from app.models import Product
from app.schemas import ProductCreate


def get_products(db: Session):
    return db.query(Product).all()


def get_product_by_id(db: Session, product_id: str):
    return db.query(Product).filter(Product.id == product_id).first()


def create_product(db: Session, product: ProductCreate):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(db: Session, product: Product, updated_product: ProductCreate):
    for key, value in updated_product.dict().items():
        setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return product


def delete_product(db: Session, product: Product):
    db.delete(product)
    db.commit()
    return product
