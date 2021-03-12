from .hotel import Hotel
from typing import Iterable


class Enseigne:
    def __init__(self, nom: str, hotels: Iterable[Hotel] = []) -> None:
        self.nom = nom
        self.__hotels = set()
        for hotel in hotels:
            if hotel and not isinstance(hotel, Hotel):
                self.__hotels = set()
                raise ValueError(
                    'Le parametre hotels doit être une liste d\'hotels')
            self.__hotels.add(hotel)

    @property
    def nom(self) -> str:
        return self.__nom

    @nom.setter
    def nom(self, nom: str) -> None:
        if not isinstance(nom, str):
            raise ValueError('Le nom de l\'enseigne doit être une string')
        self.__nom = nom

    @property
    def hotels(self) -> Iterable[Hotel]:
        return self.__hotels

    def ajouter_hotel(self, hotel: Hotel) -> None:
        if not isinstance(hotel, Hotel):
            raise ValueError('Le parametre doit être un hotel')
        self.__hotels.update({hotel})
        hotel.enseigne = self

    def supprimer_hotel(self, hotel: Hotel) -> None:
        if not isinstance(hotel, Hotel):
            raise ValueError('Le parametre doit être un hotel')
        try:
            self.__hotels.remove(hotel)
            hotel.enseigne = None
        except KeyError:
            raise KeyError('L\'hotel n\'est pas dans la liste')
