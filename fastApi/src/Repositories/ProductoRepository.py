from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class ProductoRepository:
    def __init__(self, table):
        self.engine = create_engine('sqlite:///./test.db')
        self.Session = sessionmaker(bind=self.engine)
        self.conn = self.Session()
        self.table = table

    def findAll(self):
        productos = self.conn.query(self.table).all()
        self.conn.commit()
        return productos

    def findById(self, identificador):
        producto = self.conn.query(self.table).get(identificador)
        self.conn.commit()
        return producto

    def save(self, producto):
        self.conn.add(producto)
        self.conn.commit()
        return producto

    def update(self, producto, identificador):
        if self.conn.query(self.table).get(id=identificador):
            self.conn.merge(producto)
            self.conn.commit()
            return producto
        else:
            raise Exception("No existe")

    def delete(self, identificador):
        self.conn.delete(identificador)
        self.conn.commit()
        return True

