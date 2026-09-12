"""
    # Palindromes

        1.Niveau simple : Écrivez une fonction est_palindrome(mot) qui prend en entrée une
    chaîne de caractères simple (un seul mot, tout en minuscules) et renvoie Vrai s'il
    s'agit d'un palindrome, sinon Faux.
    ◦ Exemples : "radar", "kayak", "sos".

        2. Gestion de la casse : Modifiez votre fonction pour qu'elle ignore la casse. Le
    programme doit confirmer que "Laval" est bien un palindrome.

        3. Gestion des phrases : Adaptez le programme pour qu'il puisse traiter des phrases
    complètes. Il doit ignorer les espaces et les signes de ponctuation.
    ◦ Exemple célèbre : "Engage le jeu que je le gagne".
    Exemples de tests à valider :

"""


var_one = "Bonjour"
var_two = "sos"
var_three = "12321"
var_four = "kayak"
var_five = "radar"
var_six = "Esope, reste ici et se repose"
var_seven = "Et la marine va venir à malte" # XXXXXXX
var_huit = "Engage le jeu que je le gagne"

"""
table_codes = {
    224: "a",  # à
    226: "a",  # â
    230: "ae", # æ
    231: "c",  # ç
    232: "e",  # è
    233: "e",  # é
    234: "e",  # ê
    235: "e",  # ë
    238: "i",  # î
    239: "i",  # ï
    244: "o",  # ô
    339: "oe", # œ
    249: "u",  # ù
    251: "u",  # û
    252: "u",  # ü
    255: "y"   # ÿ
}
"""


def is_palindrome(txt):
    valid_letters = [chr(i) for i in range(ord("a"), ord("z"))]
    cleaned_txt = ""
    results = 0
    for l in txt.lower():
        if l in valid_letters or ord(l) >= 224 and ord(l) <= 255 :
            cleaned_txt += l
    for i, l in enumerate(cleaned_txt):
        if not l == cleaned_txt[-i - 1]:
            results +=1
    if results == 0:
        return True
    else:
        return False

print(is_palindrome(var_three))




