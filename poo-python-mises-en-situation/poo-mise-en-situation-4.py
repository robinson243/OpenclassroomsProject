# POO EXERCICE DE MISE EN SITUATION 4

# ---
class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom)

# ---
noms = []
for i in range(3):
    noms.append(input(f"nom de la personne {i+1} : "))

# noms.append(input("nom de la personne 2 : "))
# noms.append(input("nom de la personne 3 : "))

l = []

for nom in noms:
    l.append(Personne(nom))

for p in l:
    p.SePresenter()