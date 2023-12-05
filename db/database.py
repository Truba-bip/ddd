from dotenv import dotenv_values
from pymongo import MongoClient
config = dotenv_values(".env")
database_client  = MongoClient(config["ATLAS_URI"])
database = database_client[config["MAGAZ"]]