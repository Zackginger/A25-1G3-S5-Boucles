import pytest
from ExDebug1 import environnement_optimal

#test_unitaire pour fonction optimal
def test_environement_optimal():
    #prep variable d'entré
    temperature= 25
    poussiere="faible"
    humidite=40
    resultat_attendu= "Tout est sous contrôle!"

    #appeler fonction
    resultatobtenue = environnement_optimal(temperature,poussiere,humidite)

    #asser verifier resultat
    assert resultat_attendu == resultatobtenue

def test_environement_optimal2():
    #prep variable d'entré
    temperature= 30
    poussiere="faible"
    humidite=40
    resultat_attendu= "Environnement non optimal"

    #appeler fonction
    resultatobtenue = environnement_optimal(temperature,poussiere,humidite)

    #asser verifier resultat
    assert resultat_attendu == resultatobtenue


def test_environement_optimal3():
    #prep variable d'entré
    temperature= 25
    poussiere="faible"
    humidite=20
    resultat_attendu= "Environnement non optimal"

    #appeler fonction
    resultatobtenue = environnement_optimal(temperature,poussiere,humidite)

    #asser verifier resultat
    assert resultat_attendu == resultatobtenue

def test_environement_optimal4():
    #prep variable d'entré
    temperature= 30
    poussiere="moyen"
    humidite=25
    resultat_attendu= "Environnement non optimal"

    #appeler fonction
    resultatobtenue = environnement_optimal(temperature,poussiere,humidite)

    #asser verifier resultat
    assert resultat_attendu == resultatobtenue