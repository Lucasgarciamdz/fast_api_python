from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer

BaseModel = declarative_base()


class MyModel(BaseModel):
    """SQLAlchemy model for the 'my_model' table."""

    __tablename__ = 'my_model'
    id = Column(Integer, primary_key=True, autoincrement=True)
