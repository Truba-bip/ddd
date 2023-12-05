from .mongo_repository import MongoRepository

class OrderRepository(MongoRepository):
    collection_name = "orders"