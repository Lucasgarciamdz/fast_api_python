from fastapi import APIRouter, HTTPException, status
from typing import List
from fastApi.src.Services.ProductoServiceImp import ProductoServiceImpl
from fastApi.src.Models.ProductoModel import ProductoModel
from fastApi.src.Entities.Producto import Producto
from fastApi.src.Controllers.BaseController import BaseController

routerProducto = APIRouter()


class ProductoControllerImplement(BaseController):
    """Controller for handling operations related to Products."""

    @routerProducto.get("", response_model=List[Producto])
    def get_all(self):
        """Fetch all products."""
        try:
            productos = ProductoServiceImpl.findAll()
            if not productos:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No products found")
            return productos
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    @routerProducto.get("/{id}", response_model=ProductoModel)
    def get_one(self, id: int):
        """Fetch a product by its ID."""
        try:
            producto = ProductoServiceImpl.findOne(id)
            if not producto:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No product found with ID {id}")
            return producto
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    @routerProducto.post("", response_model=Producto)
    def save(self, producto: ProductoModel):
        """Create a new product."""
        try:
            return ProductoServiceImpl.save(producto)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    @routerProducto.delete("/{id}", response_model=str)
    def delete(self, id: int):
        """Delete a product by its ID."""
        try:
            success = ProductoServiceImpl.delete(id)
            if not success:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Failed to delete product with ID {id}")
            return "Product deleted"
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    @routerProducto.put("/{id}", response_model=Producto)
    def update(self, id: int, producto: ProductoModel):
        """Update a product by its ID."""
        try:
            return ProductoServiceImpl.update(producto, id)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
