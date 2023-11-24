import pymongo
from config import settings
import os


class MongoDBPersister:
    def __init__(self):
        host = (
            os.getenv("MONGO_HOST") if os.getenv("MONGO_HOST") else settings.MONGO_HOST
        )
        port = int(
            os.getenv("MONGO_PORT") if os.getenv("MONGO_PORT") else settings.MONGO_PORT
        )
        db_name = (
            os.getenv("MONGO_DB_NAME")
            if os.getenv("MONGO_DB_NAME")
            else settings.MONGO_DB_NAME
        )
        collection_name = (
            os.getenv("MONGO_COLLECTION_NAME")
            if os.getenv("MONGO_COLLECTION_NAME")
            else settings.MONGO_COLLECTION_NAME
        )

        self.client = pymongo.MongoClient(host, port)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def get_objects(self, filter_date, filter_option):
        query = {
            # "fecha_creacion": filter_date,
            "tipo_sorteo": filter_option,
        }
        return self.collection.find(query)

    def close_connection(self):
        self.client.close()
