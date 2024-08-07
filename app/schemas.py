from pydantic import BaseModel


class ProductCreate(BaseModel):
    id: str
    name: str
    price: float
    stock: int
    urlImage: str
    description: str
    v: int


class ProductResponse(ProductCreate):
    pass
