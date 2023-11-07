from abc import ABC, abstractmethod
from typing import Any


class BaseController(ABC):
    """Abstract base class for controllers."""

    @abstractmethod
    def get_all(self) -> Any:
        """Fetch all objects. To be implemented by subclasses."""
        pass

    @abstractmethod
    def get_one(self, id: int) -> Any:
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
