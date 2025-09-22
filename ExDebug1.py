


def environnement_optimal(temperature, poussiere, humidite):
    """
    Vérifie si l'environnement d'un ordinateur est optimal.

    Paramètres :
    - temp : température en °C (int ou float)
    - poussiere : niveau de poussière ("faible", "moyen", "élevé")
    - humidite : taux d’humidité en % (int ou float)

    Retour :
    - "Tout est sous contrôle!" si toutes les conditions sont respectées
    - "Environnement non optimal" sinon (après avoir affiché les problèmes détectés)
    """

    alerte = False

    # Vérification température
    if temperature < 18:
        print("Température trop basse")
        alerte = True
    elif temperature > 27:
        print("Température trop élevée")
        alerte = True

    # Vérification humidité
    if humidite <= 30:
        print("Humidité trop basse")
        alerte = True
    elif humidite >= 50:
        print("Humidité trop élevée")
        alerte = True

    # Vérification poussière
    if poussiere != "faible":
        print("Trop de poussière")
        alerte = True

    # Retour final
    if not alerte:
        return "Tout est sous contrôle!"
    else:
        return "Environnement non optimal"
listtemp=[]
listpous=[]
listhum=[]

if __name__ == "__main__":
    for i in range(3):
        while True:
            try:
                temps=float(input("entrer la température: "))
                poussière = input("entrer le niveau de poussière: ")
                humiditer = float(input("quelle est l'humidité: "))
                if temps<0 and humiditer<0 and poussière != "moyen" and poussière != "faible" and poussière !="élevé":
                    listtemp.append(temps)
                    listpous.append(poussière)
                    listhum.append(humiditer)
                    break
            except:
                print("😡😡😡not a valid anwser😡😡😡")
        print(environnement_optimal(temps, poussière, humiditer))
    print("Les température:")
    print("-".join(listtemp))
    print("Les niveaux de poussière")
    print("-".join(listpous))
    print("Les niveaux d'humidité")
    print("-".join(listhum))
