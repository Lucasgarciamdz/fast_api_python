from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import uvicorn
from fastApi.src.Controllers.ProductoController import routerProducto
from fastApi.src.Controllers.RatingController import routerRating
app = FastAPI()
Base = declarative_base()

app.include_router(routerProducto, prefix="/producto", tags=["productos"])
app.include_router(routerRating, prefix="/rating", tags=["ratings"])

DATABASE_URL = "sqlite:///./test.db"

if not os.path.exists("../../test.db"):
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
