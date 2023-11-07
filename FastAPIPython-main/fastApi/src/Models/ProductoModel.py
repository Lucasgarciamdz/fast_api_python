from pydantic import BaseModel

class ProductoModel(BaseModel):
    id: int
    titulo: str
    precio_compra: float
    descripcion: str
    categoria: str
    imagen: str
    rating_id: int
