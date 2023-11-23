from api_consumer.quiniela import Quiniela_Client
from database import persister
from typing import Optional

import typer
from typing_extensions import Annotated


def main(
    fecha_sorteo: Annotated[Optional[str], typer.Argument()] = None,
    is_truncate: Annotated[bool, typer.Option(help="Truncate?")] = True,
):
    """
    La fecha de sorteo debe ser en formato YYYY-MM-DD, en caso de no especificarla se obtendrán los sorteos del día actual.

    """

    qc = Quiniela_Client()
    p = persister.MongoDBPersister(is_truncate=is_truncate)

    if fecha_sorteo:
        sorteos = qc.get_sorteos(sorteo_date=fecha_sorteo)
    else:
        sorteos = qc.get_sorteos()

    for s in sorteos:
        sorteo_id = s["id"]
        extracto = qc.get_extracto(sorteo_id)

        for e in extracto:
            p.persist_object(e)


if __name__ == "__main__":
    typer.run(main)
