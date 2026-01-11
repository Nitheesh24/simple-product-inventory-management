from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    category: str
    price: float
    stock_quantity: int

class ProductUpdate(BaseModel):
    stock_quantity: int

class ProductResponse(ProductCreate):
    id: int

    class Config:
        from_attributes = True
