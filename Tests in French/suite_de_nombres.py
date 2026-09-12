"""
Écrire une fonction create_intervals(numbers) qui reçoit une liste d'entiers triés par ordre croissant et les transforme
en une chaîne de caractères simplifiée.

Règles de formatage :
        Séquences consécutives : Si plusieurs nombres se suivent (ex: 5, 6, 7), ils doivent être représentés par
        la plage "début-fin" (ex: "5-7").
        Nombres isolés : Si un nombre n'a pas de successeur ou de prédécesseur immédiat dans la liste, il doit
        apparaître seul.
        Séparateur : Chaque élément (nombre seul ou plage) doit être séparé par une virgule et un espace (, ).

Format des données
    Entrée : Une liste d'entiers triés (List[int]).
    Sortie : Une chaîne de caractères (str).

Exemples:

Exemple 1 : Cas standard (Mélange de plages et isolés)
    Entrée : [2, 3, 5, 6, 7, 10, 12]
    Sortie attendue : "2-3, 5-7, 10, 12"

Exemple 2 : Séquence continue
    Entrée : [1, 2, 3, 4, 5]
    Sortie attendue : "1-5"

Exemple 3 : Aucun nombre consécutif
    Entrée : [1, 3, 5, 7]
    Sortie attendue : "1, 3, 5, 7"

Exemple 4 : Liste vide ou élément unique
    Entrée : [] -> Sortie : ""
    Entrée : [42] -> Sortie : "42"
"""

# START
one = [2, 3, 5, 6, 7, 10, 12]
two = [1, 2, 3, 4, 5]
three = [1, 3, 5, 7]
four = []
five = [42]

def create_intervals(numbers) :
    if not numbers:
        return ""

    output = f"{numbers[0]}"

    for i in range(1, len(numbers) -1):
        if numbers[i] == numbers[i +1] -1:
            if numbers[i] != numbers[i -1] +1:
                output += f",{numbers[i]}"
            elif numbers[i] == numbers[-1]:
                output += f", {numbers[i]}"
        elif numbers[i] == numbers[i -1] +1:
            output += f"-{numbers[i]}"
        else:
            output += f",{numbers[i]}"
    if len(numbers) > 1:
        output += f",{numbers[-1]}"

    return output

print(create_intervals(five))