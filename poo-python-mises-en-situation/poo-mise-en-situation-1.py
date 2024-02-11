# POO EXERCICE DE MISE EN SITUATION 1
# genre
#   False : Femme
#   True  : Homme
class Personne:
    def __init__(self, nom: str, age: int, genre: bool):
        self.nom = nom  # crée une variable d'instance : nom
        self.age = age
        self.genre = genre
        print("Constructeur personne " + self.nom)

    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur
        print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")
        gender = "Masculin" if self.genre else "Feminin"
        e_option = "e" if not self.genre else ""
        print(f"Genre {gender}")

        if self.EstMajeur():
            print(f"Je suis majeur{e_option}")
        else:
            print(f"Je suis mineur{e_option}")

    def EstMajeur(self):
        return self.age >= 18


personne1 = Personne("Jean", 25, True)
personne1.SePresenter()

personne2 = Personne("Emilie", 17, False)
personne2.SePresenter()
