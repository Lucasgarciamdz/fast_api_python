from pydantic import BaseModel
from typing import Optional


class RatingModel(BaseModel):
    """Data model for the 'Rating' table."""

    id: Optional[int] = None
    rate: float
    contador: int
