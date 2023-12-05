from typing import Annotated, List
from fastapi import APIRouter, Body, Depends, HTTPException, Request, Response
from api.dependencies import users_service
from services.user_services import UserService
from models.user import User,AddUser,UpdateUser


router = APIRouter()

@router.post("/add",response_model=User,response_description="Создание нового пользователя")
async def add_user(request:Request,user_service:Annotated[UserService,Depends(users_service)],user:AddUser= Body(...)):
    result = await user_service.add_user(user)
    return result

@router.get("/{id}",response_description="Получение пользователя по id",response_model=User)
async def get_user(id:str,request:Request,user_service:Annotated[UserService,Depends(users_service)]):
    user= await user_service.get_user(id)
    if(user is not None):
        return user
    raise HTTPException(status_code=404,detail="Пользователя с таким id не найден")

@router.get("/",response_description="Получение всех пользователей",response_model=List[User])
async def get_user(request:Request,response:Response,user_service:Annotated[UserService,Depends(users_service)]):
    users = await user_service.get_all_user()
    return users

@router.delete("/{id}",response_description="Удаление пользователя по указанному id")
async def delete_user(id:str,request:Request,response:Response,user_service:Annotated[UserService,Depends(users_service)]):
    result = await user_service.delete_user(id)
    if result == 1:
        response.status_code = 204
        return response
    raise HTTPException(status_code=404,detail="Пользователь с таким id не найден")
    
@router.put("/{id}",response_description="Обновление данных о пользователе",response_model=User)
async def update_user(id:str,user:UpdateUser,request:Request,user_service:Annotated[UserService,Depends(users_service)]):
    result = await user_service.update_user(id,user)
    if result == 1:
        if(update_user := await user_service.get_user(id))is not None:
            return update_user
    raise HTTPException(status_code=404,detail="Пользователь с таким id не найден")
        
