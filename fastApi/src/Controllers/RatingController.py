from fastapi import APIRouter, HTTPException
from typing import List
from fastApi.src.Services.RatingServiceImp import RatingServiceImpl
from fastApi.src.Models.RatingModel import RatingModel
from fastApi.src.Entities.Rating import Rating
from fastApi.src.Controllers.BaseController import BaseController

routerRating = APIRouter()

class RatingControllerImplement(BaseController):

    @routerRating.get("/", response_model=List[Rating])
    def get_all_ratings(self):
        try:
            ratings = RatingServiceImpl.findAll()
            if not ratings:
                raise HTTPException(status_code=404, detail="No se encontraron registros de rating")
            return ratings
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @routerRating.get("/{id}", response_model=Rating)
    def get_rating_by_id(self, id: int):
        try:
            rating = RatingServiceImpl.findOne(id)
            if not rating:
                raise HTTPException(status_code=404, detail=f"No se encontró un registro coincidente con el ID {id}")
            return rating
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @routerRating.post("/", response_model=Rating)
    def create_rating(self, rating: RatingModel):
        try:
            return RatingServiceImpl.save(rating)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @routerRating.delete("/{id}", response_model=str)
    def delete_rating(self, id: int):
        try:
            success = RatingServiceImpl.delete(id)
            if not success:
                raise HTTPException(status_code=404, detail=f"No se pudo eliminar el registro en rating")
            return "Registro eliminado"
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @routerRating.put("/{id}", response_model=Rating)
    def update_rating(self, id: int, rating: RatingModel):
        try:
            return RatingServiceImpl.update(rating, id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
