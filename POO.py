# coding=utf-8
# Première partie ave les classes et les attributs


class Humain:
    humaincrees = 0

    def __init__(self, prenom, age):
        print("Création d'un humain...")
        self.prenom = prenom
        self.age = age
        Humain.humaincrees += 1


print("Lancement du programme")
h1 = Humain("Toto", 25)
print(f"Il s'appelle {h1.prenom} et il a {h1.age} ans")
print(f"Humain existant : {Humain.humaincrees}")
h2 = Humain("Tata", 17)
print(f"Il s'appelle {h2.prenom} et il a {h2.age} ans")
print(f"Humain existant : {Humain.humaincrees}")
