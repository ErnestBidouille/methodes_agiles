Feature: US_002 Calculer le prix d'une famille
    En tant que directeur
    Je veux calculer le prix d'une famille en lui appliquant une remise
    Afin de lui faire payer le prix indiqué

    Scenario Outline: Calculer le coût d'une famille
        Given Un directeur avec un hotel à <prix> euros.
        When On calcule le prix pour une famille de <nb_personnes> avec une remise de <remise>
        Then Le prix total est de <total>

        Examples:
            | prix | nb_personnes | remise | total |
            | 50   | 4            | 25     | 175   |
            | 150  | 8            | 120    | 1080  |
