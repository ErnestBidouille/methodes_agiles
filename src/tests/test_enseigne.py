import pytest
from typing import Set
from ..app.enseigne import Enseigne
from ..app.hotel import Hotel


@pytest.fixture()
def get_nom_enseigne() -> str:
    return 'Les Mercure'


@pytest.fixture()
def get_hotels() -> Set[Hotel]:
    hotel = Hotel("Test Mercure", 80)
    hotel2 = Hotel("Test2 Mercure", 85)
    return {hotel, hotel2}


@pytest.fixture()
def get_enseigne(get_nom_enseigne, get_hotels) -> Enseigne:
    return Enseigne(get_nom_enseigne, get_hotels)


def test_get_nom_enseigne(get_enseigne, get_nom_enseigne):
    assert get_enseigne.nom == get_nom_enseigne


def test_set_nom_enseigne(get_enseigne):
    nouveau_nom = 'Nouveau nom'
    get_enseigne.nom = nouveau_nom
    assert get_enseigne.nom == nouveau_nom
    with pytest.raises(ValueError):
        get_enseigne.nom = 1
    with pytest.raises(ValueError):
        get_enseigne.nom = range(1)


def test_init_enseigne(get_nom_enseigne, get_hotels):
    enseigne = Enseigne(get_nom_enseigne, get_hotels)
    assert enseigne.hotels == get_hotels
    enseigne = Enseigne('Enseigne Test')
    assert enseigne.hotels == set()
    enseigne = Enseigne('Enseigne Test', [])
    assert enseigne.hotels == set()
    with pytest.raises(ValueError):
        Enseigne(1, get_hotels)
    with pytest.raises(ValueError):
        Enseigne(get_nom_enseigne, ['Hotel1'])


def test_ajouter_hotel(get_enseigne, get_hotels):
    hotel = Hotel('Test hotel', 50)
    get_enseigne.ajouter_hotel(hotel)
    assert get_enseigne.hotels == {*get_hotels, hotel}
    with pytest.raises(ValueError):
        get_enseigne.ajouter_hotel('Hotel')


def test_supprimer_hotel(get_enseigne, get_hotels):
    print(len(get_enseigne.hotels))
    get_enseigne.supprimer_hotel(get_hotels.pop())
    print(len(get_enseigne.hotels), flush=True)
    assert get_enseigne.hotels == get_hotels
    with pytest.raises(ValueError):
        get_enseigne.supprimer_hotel('Hotel')
    with pytest.raises(KeyError):
        get_enseigne.supprimer_hotel(Hotel('Nouvel hotel', 50))
