from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import Type, Optional
from Entities.Producto import Producto


class ProductoRepository:
    """Repository class for handling operations related to the 'Producto' table."""

    def __init__(self, table: Type[Producto]):
        self.engine = create_engine('sqlite:///./test.db')
        self.Session = sessionmaker(bind=self.engine)
        self.table = table

    def findAll(self) -> Optional[list[Producto]]:
        """Fetch all products."""
        with Session(self.engine) as session:
            productos = session.query(self.table).all()
            return productos

    def findById(self, identificador: int) -> Optional[Producto]:
        """Fetch a product by its ID."""
        with Session(self.engine) as session:
            producto = session.query(self.table).get(identificador)
            return producto

    def save(self, producto: Producto) -> Producto:
        """Save a product."""
        with Session(self.engine) as session:
            session.add(producto)
            session.commit()
            return producto

    def update(self, producto: Producto, identificador: int) -> Optional[Producto]:
        """Update a product by its ID."""
        with Session(self.engine) as session:
            if session.query(self.table).get(id=identificador):
                session.merge(producto)
                session.commit()
                return producto
            else:
                raise Exception("Product does not exist")

    def delete(self, identificador: int) -> bool:
        """Delete a product by its ID."""
        with Session(self.engine) as session:
            producto = session.query(self.table).get(identificador)
            if producto:
                session.delete(producto)
                session.commit()
                return True
            else:
                raise Exception("Product does not exist")
