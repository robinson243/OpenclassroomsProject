# coding=utf-8

"""
Méthode                 : fonction sur une instance (ex : manger, marcher, courrir)
Méthode de classe       : fonction sur une classe 
Méthode classique       : fonction indépendante mais "lié" à une classe 
"""


class Humain:
    lieu_habitation = "Terre"

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def parler(self, msg):  # self = Méthode standard
        print(f"{self.nom} a dit : {msg}")

    def changer_planete(cls, nouvelle_planete):  # clas = Méthode de classe
        Humain.lieu_habitation = nouvelle_planete
    
    changer_planete = classmethod(changer_planete)
    
    def defintion():
        print("L'Humain est classé comme étant le plus haut etre-vivant de la chaine alimentaire")
    defintion = staticmethod(defintion)
# Programme Principal

h1 = Humain("Jason", 26)

Humain.changer_planete("Mars")
Humain.defintion()

print(f"Planète actuelle : {Humain.lieu_habitation}")
