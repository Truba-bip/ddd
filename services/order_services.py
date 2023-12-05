from fastapi.encoders import jsonable_encoder
from models.order import UpdateOrder, AddOrder
from repositories.repository import AbstractRepository


class OrderService:
    def __init__(self, order_rep:AbstractRepository):
        self.order_rep = order_rep()
    
    async def add_order(self,order:AddOrder):
        order = jsonable_encoder(order)
        result = await self.order_rep.add(order)
        return result 
    
    async def update_order(self,id,order:UpdateOrder):
        order= jsonable_encoder(order)
        result = await self.order_rep.update(id,order)
        return result 
    
    async def get_all_order(self):
        orders= await self.order_rep.get_all()
        return orders
    
    async def get_order(self,id):
       order = await self.order_rep.get(id)
       return order
   
    async def delete_order(self,id):
        result = await self.order_rep.delete(id)
        return result
    