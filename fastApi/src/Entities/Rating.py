from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Float
from ..main import Base


class Rating(Base):
    """SQLAlchemy model for the 'Rating' table."""

    __tablename__ = 'Rating'
    id = Column(Integer, primary_key=True)
    rate = Column(Float, nullable=False)
    contador = Column(Integer, nullable=False)

    producto = relationship('Producto', back_populates='rating')
