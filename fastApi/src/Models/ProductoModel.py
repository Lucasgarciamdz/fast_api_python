from pydantic import BaseModel
from typing import Optional


class ProductoModel(BaseModel):
    """Data model for the 'Producto' table."""

    id: Optional[int] = None
    titulo: str
    precio_compra: float
    descripcion: str
    categoria: str
    imagen: str
    rating_id: int
