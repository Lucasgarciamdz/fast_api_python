from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class RatingRepository:
    def __init__(self, table):
        self.engine = create_engine('sqlite:///./test.db')
        self.Session = sessionmaker(bind=self.engine)
        self.conn = self.Session()
        self.table = table

    def findAll(self):
        ratings = self.conn.query(self.table).all()
        self.conn.commit()
        return ratings

    def findById(self, identificador):
        rating = self.conn.query(self.table).get(identificador)
        self.conn.commit()
        return rating

    def save(self, rating):
        self.conn.add(rating)
        self.conn.commit()
        return rating

    def update(self, rating, identificador):
        if self.conn.query(self.table).get(id=identificador):
            self.conn.merge(rating)
            self.conn.commit()
            return rating
        else:
            raise Exception("No existe")

    def delete(self, identificador):
        self.conn.delete(identificador)
        self.conn.commit()
        return True

