from pydantic import BaseModel

class RatingModel(BaseModel):
    id: int
    rate: float
    contador: int
