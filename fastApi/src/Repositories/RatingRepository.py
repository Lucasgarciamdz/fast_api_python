from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import Type, Optional
from Entities.Rating import Rating


class RatingRepository:
    """Repository class for handling operations related to the 'Rating' table."""

    def __init__(self, table: Type[Rating]):
        self.engine = create_engine('sqlite:///./test.db')
        self.Session = sessionmaker(bind=self.engine)
        self.table = table

    def findAll(self) -> Optional[list[Rating]]:
        """Fetch all ratings."""
        with Session(self.engine) as session:
            ratings = session.query(self.table).all()
            return ratings

    def findById(self, identificador: int) -> Optional[Rating]:
        """Fetch a rating by its ID."""
        with Session(self.engine) as session:
            rating = session.query(self.table).get(identificador)
            return rating

    def save(self, rating: Rating) -> Rating:
        """Save a rating."""
        with Session(self.engine) as session:
            session.add(rating)
            session.commit()
            return rating

    def update(self, rating: Rating, identificador: int) -> Optional[Rating]:
        """Update a rating by its ID."""
        with Session(self.engine) as session:
            if session.query(self.table).get(id=identificador):
                session.merge(rating)
                session.commit()
                return rating
            else:
                raise Exception("Rating does not exist")

    def delete(self, identificador: int) -> bool:
        """Delete a rating by its ID."""
        with Session(self.engine) as session:
            rating = session.query(self.table).get(identificador)
            if rating:
                session.delete(rating)
                session.commit()
                return True
            else:
                raise Exception("Rating does not exist")
