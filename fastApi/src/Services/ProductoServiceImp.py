from .BaseService import BaseService
from ..Repositories.ProductoRepository import ProductoRepository
from ..Entities import Producto


class ProductoServiceImpl(BaseService):

    def __init__(self):
        self.repository = ProductoRepository(table=Producto)

    def findAll(self):
        try:
            return self.repository.findAll()
        except Exception as e:
            raise Exception(str(e))

    def findOne(self, identificador):
        try:
            return self.repository.findById(identificador)
        except Exception as e:
            raise Exception(str(e))

    def save(self, entity):
        try:
            return self.repository.save(entity)
        except Exception as e:
            raise Exception(str(e))

    def update(self, entity, identificador):
        try:
            optEntity = self.repository.findById(identificador)
            if optEntity:
                entityUpdate = self.repository.save(entity)
                return entityUpdate
        except Exception as e:
            raise Exception(str(e))

    def delete(self, identificador):
        try:
            if self.repository.findById(identificador):
                self.repository.delete(identificador)
                return True
            else:
                raise Exception()
        except Exception as e:
            raise Exception(str(e))