from abc import  ABC, abstractmethod

class BaseController(ABC):

    @abstractmethod
    def getAll(self):
        pass

    @abstractmethod
    def getOne(self, id):
        pass

    @abstractmethod
    def save(self, object):
        pass

    @abstractmethod
    def update(self, object, id):
        pass

    @abstractmethod
    def delete(self, id):
        pass