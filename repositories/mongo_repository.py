from bson import ObjectId
from .repository import AbstractRepository
from db.database import database


class MongoRepository(AbstractRepository):
    collection_name:str
    async def get_all(self):
        result = database[self.collection_name].find(limit=100)
        return list(result)
    async def get(self,id):
        result = database[self.collection_name].find_one({"_id": ObjectId(id)})
        return result
    async def add(self,entity):
        new_entity = database[self.collection_name].insert_one(entity)
        result =  database[self.collection_name].find_one({"_id": new_entity.inserted_id})
        return result
    async def delete(self,id):
        delete_result = database[self.collection_name].delete_one({"_id": ObjectId(id)})
        return delete_result.deleted_count
    async def update(self,id,update_entity):
        update_result = database[self.collection_name].update_one({"_id":ObjectId(id)},{"$set":update_entity})
        return update_result.modified_count
        