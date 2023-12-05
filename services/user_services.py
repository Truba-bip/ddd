from fastapi.encoders import jsonable_encoder
from models.user import UpdateUser, AddUser
from repositories.repository import AbstractRepository

class UserService:
    def __init__(self, user_rep:AbstractRepository):
        self.user_rep = user_rep()
    
    async def add_user(self,user:AddUser):
        user = jsonable_encoder(user)
        result = await self.user_rep.add(user)
        return result 
    async def update_user(self,id,user:UpdateUser):
        user= jsonable_encoder(user)
        result = await self.user_rep.update(id,user)
        return result 
    async def get_all_user(self):
        users = await self.user_rep.get_all()
        return users
    async def get_user(self,id):
       user = await self.user_rep.get(id)
       return user
    async def delete_user(self,id):
        result = await self.user_rep.delete(id)
        return result
    