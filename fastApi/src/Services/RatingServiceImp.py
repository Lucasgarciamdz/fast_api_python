from .BaseService import BaseService
from ..Repositories.RatingRepository import RatingRepository
from Entities.Rating import Rating
from typing import Optional


class RatingServiceImpl(BaseService):
    """Service implementation for handling operations related to the 'Rating' table."""

    def __init__(self):
        self.repository = RatingRepository(table=Rating)

    def find_all(self) -> Optional[list[Rating]]:
        """Fetch all ratings."""
        return self.repository.findAll()

    def find_one(self, identificador: int) -> Optional[Rating]:
        """Fetch a rating by its ID."""
        return self.repository.findById(identificador)

    def save(self, entity: Rating) -> Rating:
        """Save a rating."""
        return self.repository.save(entity)

    def update(self, entity: Rating, identificador: int) -> Optional[Rating]:
        """Update a rating by its ID."""
        optEntity = self.repository.findById(identificador)
        if optEntity:
            entityUpdate = self.repository.save(entity)
            return entityUpdate
        else:
            raise Exception("Rating does not exist")

    def delete(self, identificador: int) -> bool:
        """Delete a rating by its ID."""
        if self.repository.findById(identificador):
            self.repository.delete(identificador)
            return True
        else:
            raise Exception("Rating does not exist")
