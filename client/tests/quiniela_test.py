from api_consumer.quiniela import Quiniela_Client


def test_quiniela_client_default():
    qc = Quiniela_Client()
    assert qc.get_sorteos() is not None or qc.get_sorteos() == []


def test_quiniela_client_with_valid_date():
    qc = Quiniela_Client()
    assert len(qc.get_sorteos(sorteo_date="2023-10-14")) > 0
