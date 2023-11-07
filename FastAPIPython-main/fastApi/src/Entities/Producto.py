from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from ..main import Base

class Producto(Base):
    __tablename__ = 'Producto'
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    precio_compra = Column(Float)
    descripcion = Column(String)
    categoria = Column(String)
    imagen = Column(String)
    rating_id = Column(Integer, ForeignKey('Rating.id'))

    rating = relationship('Rating', back_populates='Producto')
