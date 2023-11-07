from abc import ABC, abstractmethod
from typing import Any


class BaseService(ABC):
    """Abstract base class for services."""

    @abstractmethod
    def find_all(self) -> Any:
        """Fetch all objects. To be implemented by subclasses."""
        pass

    @abstractmethod
    def find_one(self, id: int) -> Any:
        """Fetch a single object by its ID. To be implemented by subclasses."""
        pass

    @abstractmethod
    def save(self, obj: Any) -> Any:
        """Save an object. To be implemented by subclasses."""
        pass

    @abstractmethod
    def update(self, obj: Any, id: int) -> Any:
        """Update an object by its ID. To be implemented by subclasses."""
        pass

    @abstractmethod
    def delete(self, id: int) -> Any:
        """Delete an object by its ID. To be implemented by subclasses."""
        pass
