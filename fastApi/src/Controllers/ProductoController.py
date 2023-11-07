from fastapi import APIRouter, HTTPException
from typing import List
from fastApi.src.Services.ProductoServiceImp import ProductoServiceImpl
from fastApi.src.Models.ProductoModel import ProductoModel
from fastApi.src.Entities.Producto import Producto
from fastApi.src.Controllers.BaseController import BaseController

routerProducto = APIRouter()


class ProductoControllerImplement(BaseController):

    @routerProducto.get("", response_model=List[Producto])
    def get_all(self):
        try:
            productos = ProductoServiceImpl.findAll()
            if not productos:
                raise HTTPException(status_code=404, detail="Productos no encontrados")
            return productos
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @routerProducto.get("/{id}", response_model=ProductoModel)
    def get_one(self, id: int):
        try:
            producto = ProductoServiceImpl.findOne(id)
            if not producto:
                raise HTTPException(status_code=404, detail=f"No se encontró un producto con el ID {id}")
            return producto
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @routerProducto.post("", response_model=Producto)
    def save(self, producto: ProductoModel):
        try:
            return ProductoServiceImpl.save(producto)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @routerProducto.delete("/{id}", response_model=str)
    def delete(self, id: int):
        try:
            success = ProductoServiceImpl.delete(id)
            if not success:
                raise HTTPException(status_code=404, detail=f"No se pudo eliminar el registro en producto")
            return "Registro eliminado"
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @routerProducto.put("/{id}", response_model=Producto)
    def update(self, id: int, producto: ProductoModel):
        try:
            return ProductoServiceImpl.update(producto, id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
