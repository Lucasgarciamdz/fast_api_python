from abc import ABC, abstractmethod

class BaseService(ABC):

    @abstractmethod
    def findAll(self):
        pass

    @abstractmethod
    def findOne(self, identificador):
        pass

    @abstractmethod
    def save(self, entity):
        pass

    @abstractmethod
    def update(self, entity, identificador):
        pass

    @abstractmethod
    def delete(self, identificador):
        pass