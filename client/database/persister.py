import pymongo
from config import settings
from datetime import datetime
import os


class MongoDBPersister:
    def __init__(self, truncate_date: str = None):
        truncate_date = (
            truncate_date
            if truncate_date
            else (
                datetime.strftime(
                    datetime.now(),
                    "Y-%m-%d",
                ),
            )
        )

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

        self.truncate_collection_by_date(truncate_date)

    def truncate_collection_by_date(self, truncate_date: str) -> int:
        result = self.collection.delete_many({"fecha_creacion": truncate_date})
        return result.deleted_count

    def persist_object(self, data):
        document = {
            "id_sorteo": data.get("id"),
            "extracto": data.get("extracto"),
            "fecha_creacion": datetime.strftime(
                datetime.strptime(data.get("fecha_creacion"), "%Y-%m-%dT%H:%M:%S.%f"),
                "Y-%m-%d",
            ),
            "posicion": data.get("posicion"),
            "numero": data.get("numero"),
            "tipo_sorteo": data.get("tipo_sorteo"),
        }
        result = self.collection.insert_one(document)
        return result.inserted_id

    def close_connection(self):
        self.client.close()
