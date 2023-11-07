from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from ..main import Base


class Producto(Base):
    """SQLAlchemy model for the 'Producto' table."""

    __tablename__ = 'Producto'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(255), nullable=False)
    precio_compra = Column(Float, nullable=False)
    descripcion = Column(String(255), nullable=False)
    categoria = Column(String(255), nullable=False)
    imagen = Column(String(255), nullable=False)
    rating_id = Column(Integer, ForeignKey('Rating.id'))

    rating = relationship('Rating', back_populates='producto')
