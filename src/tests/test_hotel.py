import pytest
from ..app.hotel import Hotel
from ..app.enseigne import Enseigne


@pytest.fixture()
def get_hotel_nom() -> str:
    return 'Mercure Test'


@pytest.fixture()
def get_hotel_prix() -> int:
    return 80


@pytest.fixture()
def get_hotel(get_hotel_nom, get_hotel_prix) -> Hotel:
    return Hotel(get_hotel_nom, get_hotel_prix)


def test_get_prix_hotel(get_hotel, get_hotel_prix):
    assert get_hotel.prix == get_hotel_prix


def test_get_nom_hotel(get_hotel, get_hotel_nom):
    assert get_hotel.nom == get_hotel_nom


def test_set_nom_hotel(get_hotel):
    nom_test = 'Formule 1 Test'
    get_hotel.nom = nom_test
    assert get_hotel.nom == nom_test
    with pytest.raises(ValueError):
        get_hotel.nom = 'Test'
    with pytest.raises(ValueError):
        get_hotel.nom = 35000
    with pytest.raises(ValueError):
        get_hotel.nom = range(5)


def test_set_prix_hotel(get_hotel):
    prix_test = 45
    get_hotel.prix = prix_test
    assert get_hotel.prix == prix_test
    with pytest.raises(ValueError):
        get_hotel.prix = 'Test'
    with pytest.raises(ValueError):
        get_hotel.prix = -1
    with pytest.raises(ValueError):
        get_hotel.prix = range(5)


def test_prix_total(get_hotel, get_hotel_prix):
    nb_personnes_test = 5
    assert get_hotel.prix_total(
        nb_personnes_test) == get_hotel_prix * \
            nb_personnes_test


def test_get_enseigne(get_hotel):
    assert get_hotel.enseigne == None
    enseigne_test = Enseigne('Mercure Enseigne', {get_hotel})
    get_hotel.enseigne = enseigne_test
    assert get_hotel.enseigne == enseigne_test
