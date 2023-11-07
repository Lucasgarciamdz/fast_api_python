from .BaseService import BaseService
from ..Repositories.ProductoRepository import ProductoRepository
from ..Entities.Producto import Producto
from typing import Optional


class ProductoServiceImpl(BaseService):
    """Service implementation for handling operations related to the 'Producto' table."""

    def __init__(self):
        self.repository = ProductoRepository(table=Producto)

    def find_all(self) -> Optional[list[Producto]]:
        """Fetch all products."""
        return self.repository.findAll()

    def find_one(self, identificador: int) -> Optional[Producto]:
        """Fetch a product by its ID."""
        return self.repository.findById(identificador)

    def save(self, entity: Producto) -> Producto:
        """Save a product."""
        return self.repository.save(entity)

    def update(self, entity: Producto, identificador: int) -> Optional[Producto]:
        """Update a product by its ID."""
        optEntity = self.repository.findById(identificador)
        if optEntity:
            entityUpdate = self.repository.save(entity)
            return entityUpdate
        else:
            raise Exception("Product does not exist")

    def delete(self, identificador: int) -> bool:
        """Delete a product by its ID."""
        if self.repository.findById(identificador):
            self.repository.delete(identificador)
            return True
        else:
            raise Exception("Product does not exist")