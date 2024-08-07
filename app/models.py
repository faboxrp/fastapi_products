from sqlalchemy import Column, String, Integer, Float
from app.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    stock = Column(Integer)
    urlImage = Column(String)
    description = Column(String)
    v = Column(Integer)
