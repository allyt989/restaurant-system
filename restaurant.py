plats = []

while True:
    print("\n=== Restaurant Management ===")
    print("1. Add plat")
    print("2. Display plats")
    print("3. Search plat")
    print("4. Exit")

    choix = input("Choix : ")

    if choix == "1":
        nom = input("Nom du plat : ")
        prix = input("Prix : ")

        plat = {
            "nom": nom,
            "prix": prix
        }

        plats.append(plat)
        print("Plat ajouté avec succès !")

    elif choix == "2":
        print("\nListe des plats :")

        for plat in plats:
            print(f"- {plat['nom']} : {plat['prix']} €")

    elif choix == "3":
        recherche = input("Nom du plat à rechercher : ")

        trouve = False

        for plat in plats:
            if plat["nom"] == recherche:
                print(f"Plat trouvé : {plat['nom']} - {plat['prix']} €")
                trouve = True

        if not trouve:
            print("Plat non trouvé")

    elif choix == "4":
        print("Au revoir !")
        break

    else:
        print("Choix invalide")