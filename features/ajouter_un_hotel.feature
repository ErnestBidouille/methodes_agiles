Feature: US_001 Ajouter un hôtel à une enseigne
    En tant que manager d'enseigne
    Je veux ajouter un hôtel
    Afin de l'avoir dans ma liste d'hôtels à disposition
    
    Scenario: Ajouter un hotel à une enseigne
        Given Une enseigne et un hotel
        When On ajoute à l'enseigne l'hôtel
        Then L'hotel est dans la liste des hôtels
        And L'hotel a pour enseigne l'enseigne

