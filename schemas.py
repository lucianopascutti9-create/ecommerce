from pydantic import BaseModel

# --- SCHEMAS DE PRODUCTO ---
class ProductoCreate(BaseModel):
    nombre: str
    precio: float
    en_stock: bool
    categoria_id: int

class ProductoResponse(ProductoCreate):
    id: int
    
    class Config:
        from_attributes = True


# --- SCHEMAS DE CATEGORIA ---
class CategoriaBase(BaseModel):
    nombre: str

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaResponse(CategoriaBase):
    id: int
    
    class Config:
        from_attributes = True