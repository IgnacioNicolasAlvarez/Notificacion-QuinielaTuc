import pymongo
from config import settings
from datetime import datetime
import os


class MongoDBPersister:
    def __init__(self, is_truncate: bool = False):
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

        if is_truncate:
            self.collection.drop()

    def persist_object(self, data):
        document = {
            "id_sorteo": data.get("id"),
            "extracto": data.get("extracto"),
            "fecha_creacion": datetime.strptime(
                data.get("fecha_creacion"), "%Y-%m-%dT%H:%M:%S.%f"
            ),
            "posicion": data.get("posicion"),
            "numero": data.get("numero"),
        }
        result = self.collection.insert_one(document)
        return result.inserted_id

    def close_connection(self):
        self.client.close()
