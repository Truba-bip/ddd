from typing import Annotated, Optional
from bson import ObjectId
from pydantic import BaseModel, BeforeValidator,Field
from enum import Enum

PyOrderId =  Annotated[str,BeforeValidator(str)]

class StatusType(Enum):
    COMPLETE = "complete"
    NOTCOMPLETE= "not complete"
    
class Order(BaseModel):
    id:PyOrderId = Field(alias='_id', default=None)
    status:StatusType
    belongs:PyOrderId=Field() 
    class Config:
        populate_by_name = True
        json_schema_extra={
            "example":{
                "_id":"656d9d0d2a23f5f1b31a7411",
                "status":"not complete",
                "belongs":"656d9d0d2a23f5f1b31a7412"
            }
        }
        
class AddOrder(BaseModel):
    id:PyOrderId = Field(alias='_id', default=None)
    status:StatusType
    belongs:PyOrderId=Field() 
    class Config:
        populate_by_name = True
        json_schema_extra={
            "example":{
                "_id":"656d9d0d2a23f5f1b31a7411",
                "status":"not complete",
                "belongs":"656d9d0d2a23f5f1b31a7412"
            }
        }
        
class UpdateOrder(BaseModel):
    status:Optional[StatusType]
    belongs: Optional[PyOrderId]
    class Config:
        json_schema_extra={
            "example":{
                "status":"not complete",
                "belongs":"656d9d0d2a23f5f1b31a7412"
            }
        }