import pymongo
from config import settings
from datetime import datetime


class MongoDBPersister:
    def __init__(self):
        self.client = pymongo.MongoClient(settings.MONGO_HOST, settings.MONGO_PORT)
        self.db = self.client[settings.MONGO_DB_NAME]
        self.collection = self.db[settings.MONGO_COLLECTION_NAME]

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
