from fastapi import APIRouter, HTTPException, status
from typing import List
from fastApi.src.Services.RatingServiceImp import RatingServiceImpl
from fastApi.src.Models.RatingModel import RatingModel
from fastApi.src.Entities.Rating import Rating
from fastApi.src.Controllers.BaseController import BaseController

routerRating = APIRouter()


class RatingControllerImplement(BaseController):
    """Controller for handling operations related to Ratings."""

    @routerRating.get("/", response_model=List[Rating])
    def get_all_ratings(self):
        """Fetch all ratings."""
        try:
            ratings = RatingServiceImpl.findAll()
            if not ratings:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No ratings found")
            return ratings
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    @routerRating.get("/{id}", response_model=Rating)
    def get_rating_by_id(self, id: int):
        """Fetch a rating by its ID."""
        try:
            rating = RatingServiceImpl.findOne(id)
            if not rating:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No rating found with ID {id}")
            return rating
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    @routerRating.post("/", response_model=Rating)
    def create_rating(self, rating: RatingModel):
        """Create a new rating."""
        try:
            return RatingServiceImpl.save(rating)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    @routerRating.delete("/{id}", response_model=str)
    def delete_rating(self, id: int):
        """Delete a rating by its ID."""
        try:
            success = RatingServiceImpl.delete(id)
            if not success:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Failed to delete rating with ID {id}")
            return "Rating deleted"
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    @routerRating.put("/{id}", response_model=Rating)
    def update_rating(self, id: int, rating: RatingModel):
        """Update a rating by its ID."""
        try:
            return RatingServiceImpl.update(rating, id)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
