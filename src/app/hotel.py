from typing import Any


class Hotel:
    def __init__(self, nom: str, prix: int) -> None:
        self.nom = nom
        self.prix = prix
        self.enseigne = None

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
    def prix(self) -> int:
        return self.__prix

    @prix.setter
    def prix(self, prix: int) -> None:
        if not isinstance(prix, int) or prix < 0:
            raise ValueError(
                'Le paramètre prix doit être un entier supérieur ou égal à 0')
        self.__prix = prix

    @property
    def enseigne(self) -> Any:
        return self.__enseigne

    @enseigne.setter
    def enseigne(self, enseigne) -> None:
        self.__enseigne = enseigne

    def prix_total(self, nb_personnes: int) -> int:
        if nb_personnes < 1:
            raise ValueError('Il doit y avoir au moins une personne')
        return self.prix * nb_personnes
