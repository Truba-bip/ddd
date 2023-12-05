from typing import Annotated, List
from fastapi import APIRouter, Body, Depends, HTTPException, Request, Response
from api.dependencies import orders_service
from services.order_services import OrderService
from models.order import Order,AddOrder,UpdateOrder


router = APIRouter()

@router.post("/add",response_model=Order,response_description="Создание нового заказа")
async def add_order(request:Request,order_service:Annotated[OrderService,Depends(orders_service)],order:AddOrder= Body(...)):
    result = await order_service.add_order(order)
    return result

@router.get("/{id}",response_description="Получение заказа по id",response_model=Order)
async def get_order(id:str,request:Request,order_service:Annotated[OrderService,Depends(orders_service)]):
    order= await order_service.get_order(id)
    if(order is not None):
        return order
    raise HTTPException(status_code=404,detail="Заказ с таким id не найден")

@router.get("/",response_description="Получение всех заказов",response_model=List[Order])
async def get_order(request:Request,response:Response,order_service:Annotated[OrderService,Depends(orders_service)]):
    orders = await order_service.get_all_order()
    return orders

@router.delete("/{id}",response_description="Удаление заказа по указанному id")
async def delete_order(id:str,request:Request,response:Response,order_service:Annotated[OrderService,Depends(orders_service)]):
    result = await order_service.delete_order(id)
    if result == 1:
        response.status_code = 204
        return response
    raise HTTPException(status_code=404,detail="Заказ с таким id не найден")

@router.put("/{id}",response_description="Обновление данных о заказе",response_model=Order)
async def update_order(id:str,order:UpdateOrder,request:Request,order_service:Annotated[OrderService,Depends(orders_service)]):
    result = await order_service.update_order(id,order)
    if result == 1:
        if(update_order := await order_service.get_order(id))is not None:
            return update_order
    raise HTTPException(status_code=404,detail="Заказ с таким id не найден")
        
