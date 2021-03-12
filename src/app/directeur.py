from .hotel import Hotel


class Directeur:
    def __init__(self, nom: str, hotel: Hotel = None) -> None:
        self.nom = nom
        self.hotel = hotel

    @property
    def nom(self) -> str:
        return self.__nom

    @nom.setter
    def nom(self, nom: str) -> None:
        if not isinstance(nom, str) or not len(nom) >= 5:
            raise ValueError(
                'Le nom doit être une string de 5 caractères minimum')
        self.__nom = nom

    @property
    def hotel(self) -> Hotel:
        return self.__hotel

    @hotel.setter
    def hotel(self, hotel: Hotel = None) -> None:
        if hotel and not isinstance(hotel, Hotel):
            raise ValueError(
                'Le paramètre hotel n\'est pas de la classe Hotel')
        self.__hotel = hotel

    def facturer_famille(self, nb_personnes: int, remise: int = 0) -> int:
        if not self.hotel:
            raise ValueError('Le directeur n\'a pas d\'hotel associé')
        if remise < 0:
            raise ValueError('La remise doit être nulle ou positive')
        return max(self.hotel.prix_total(nb_personnes) - remise, 0)
