from typing import Annotated, Optional
from bson import ObjectId
from pydantic import BaseModel, BeforeValidator,Field

PyUserId =  Annotated[str,BeforeValidator(str)]

class User(BaseModel):
    id:PyUserId= Field(alias='_id', default=None)
    name:str=Field()
    email:str=Field()
    class Config:
        populate_by_name = True
        json_schema_extra={
            "example":{
                "_id":"",
                "name":"Ivan234",
                "email":"iva.aaa@mail.ru"
            }
        }
        
class AddUser(BaseModel):
    name:str=Field()
    email:str=Field()
    class Config:
        populate_by_name = True
        json_schema_extra={
            "example":{
                "_id":"",
                "name":"Ivan234",
                "email":"iva.aaa@mail.ru"
            }
        }
        
class UpdateUser(BaseModel):
    name:Optional[str]
    email:Optional[str]
    class Config:
        json_schema_extra={
            "example":{
                "_id":"",
                "name":"Ivan234",
                "email":"iva.aaa@mail.ru"
            }
        }