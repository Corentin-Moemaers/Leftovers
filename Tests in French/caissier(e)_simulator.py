# Enjoy

"""
Entrée: Une liste de tuples.
Format d'un tuple : (nom: str, quantite: int, prix_unitaire: float)

Sortie: Une liste de listes.
Format d'une sous-liste : [nom: str, quantite_totale: int, prix_total: float]
"""

list_one = [("Banane", 10, 0.5)]
list_two = []
list_three = [("Pomme", 3, 1.99), ("Zucchini", 1, 2.5), ("Tomate", 2, 3.0), ("Pomme", 2, 1.99)]



# First time resolving it
def calculate_price(articles):
    if not articles:
        return []

    bill = []
    articles.sort()
    name, quantity, price = articles[0]
    for i in range(1, len(articles)):
        #n = "name" | q = "quantity" | p = "price" mais du deuxième article
        n, q, p = articles[i]

        if name == n:
            quantity += q
        else:
            bill.append([name,quantity,price * quantity])
            name, quantity, price = articles[i]

    bill.append([name, quantity, quantity * price])
    return bill

print(calculate_price(list_three))





# Second time resolving it
def calculer_panier(articles):
    if not articles:
        return []

    listing = []
    sorting = sorted(list(articles))
    first_article = list(sorting[0])
    for a in range(1, len(sorting)):
        if sorting[a][0] == first_article[0]:
            first_article[1] += sorting[a][1]
        else:
            listing.append(first_article)
            first_article = list(sorting[a])
    listing.append(first_article)

    for a in range(0, len(listing)):
        listing[a][2] *= listing[a][1]

    return listing



print(calculer_panier(list_one))