from config import settings
from datetime import date
import requests


class Quiniela_Client:
    def get_sorteos(self, sorteo_date=date.today().strftime("%Y-%m-%d")) -> dict:
        response = requests.get(url=settings.URL_FECHA_SORTEO + sorteo_date)
        return response.json()

    def get_extracto(self, id_sorteo) -> dict:
        response = requests.get(url=settings.URL_EXTRACTO_SORTEO + str(id_sorteo))
        return response.json()
