from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    description: str = ""
    price: float
    quantity: int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    description: str | None = None
    price: float | None = None
    quantity: int | None = None

class ProductOut(ProductBase):
    id: int

    class Config:
        orm_mode = True
