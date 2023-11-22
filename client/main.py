from api_consumer.quiniela import Quiniela_Client
from database import persister

def main():
    qc = Quiniela_Client()
    p = persister.MongoDBPersister()
    sorteos = qc.get_sorteos()

    for s in sorteos:
        sorteo_id = s["id"]
        extracto = qc.get_extracto(sorteo_id)

        for e in extracto:
            p.persist_object(e)

if __name__ == "__main__":
    main()
