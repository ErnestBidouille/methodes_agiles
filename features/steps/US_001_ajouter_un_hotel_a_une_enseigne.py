from behave import given, when, then
from src.app.enseigne import Enseigne
from src.app.hotel import Hotel


@given('Une enseigne et un hotel')
def une_enseigne_et_un_hotel(context):
    context.enseigne = Enseigne('Mercure')
    context.hotel = Hotel('Hotel Test', 10)
    assert context.enseigne.hotels == set()


@when('On ajoute à l\'enseigne l\'hôtel')
def on_ajoute_a_l_enseigne_l_hotel(context):
    context.enseigne.ajouter_hotel(context.hotel)
    assert context.enseigne


@then('L\'hotel est dans la liste des hôtels')
def l_hotel_est_dans_la_liste_des_hotels(context):
    assert context.enseigne.hotels.pop() == context.hotel


@then('L\'hotel a pour enseigne l\'enseigne')
def l_hotel_a_pour_enseigne_l_enseigne(context):
    assert context.hotel.enseigne == context.enseigne
