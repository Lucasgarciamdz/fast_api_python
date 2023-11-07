from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from ..main import Base

class Rating(Base):
    __tablename__ = 'Rating'
    id = Column(Integer, primary_key=True)
    rate = Column(Float)
    contador = Column(Integer)

    producto = relationship('Producto', back_populates='Rating')