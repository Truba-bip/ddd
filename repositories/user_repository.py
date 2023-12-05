from .mongo_repository import MongoRepository

class UserRepository(MongoRepository):
    collection_name = "users"