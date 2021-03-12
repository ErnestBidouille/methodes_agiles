from behave import given, when, then
from src.app.directeur import Directeur
from src.app.hotel import Hotel


@given('Un directeur avec un hotel à {prix} euros.')
def un_directeur_avec_un_hotel_a_prix_euros(context, prix):
    context.directeur = Directeur('Le directeur',
                                  Hotel('Hotel Test', int(prix)))
    assert context.directeur


@when(
    'On calcule le prix pour une famille de {nb_personnes} avec une remise de {remise}'
)
def on_calcule_le_prix_pour_une_famille_de_nb_personnes_avec_une_remise(
        context, nb_personnes, remise):
    context.prix_famille = context.directeur.facturer_famille(
        int(nb_personnes), int(remise))
    assert context.prix_famille


@then('Le prix total est de {total}')
def le_prix_total_est_de_total(context, total):
    assert context.prix_famille == int(total)
