print("Veuilez saisir la liste des produits")
stock = {}
reponse = input("Voulez-vous enregistrer la liste des produits ? \n Répondez par Oui ou Non :").lower()
while (reponse == 'oui'):
    nom_produit = input("Donnez le nom du produit :")
    stock[nom_produit] = int(input("Donnez le stock :"))
    while (stock[nom_produit] < 0):
            print("Le stock doit etre un nombre positif")
            stock[nom_produit] = int(input("Donnez le stock :"))

    reponse = input("Voulez-vous continuer ? \n Répondez par Oui ou Non :").lower()

if (reponse == 'non'):
    nom_produit_vendu = input("Donnez le nom du produit vendu :").lower()
    if (nom_produit_vendu in stock.keys()):         
        nombre_ventes = int(input("Donnez le nombre de produits vendus :"))
        while (nombre_ventes < 0):
            print("Le nombre de produits vendu doit etre un nombre positif")
            stock[nom_produit] = int(input("Donnez moi le nombre de produits vendus :"))
        stock_restant = stock[nom_produit_vendu] - nombre_ventes
        if (stock_restant < 10 and stock_restant >= 0):
            print(f"Attention : stock faible. Pensez à réapprovisionner. Stock restant : {stock_restant}")
        elif (stock_restant > 10):
            print(f"Stock suffisant Stock restant : {stock_restant}")
        else:
            print(f"Impossible. Stock initial : {stock[nom_produit_vendu]}")
    else :
        print("Ce produit n'existe pas dans le stock.")