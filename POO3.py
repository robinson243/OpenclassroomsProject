# coding=utf-8

"""
Propriété : Manière de manipuler/controler des attributs
            Principe d"ncapsulation ! 
"""

class Humain:
    
    def __init__(self, nom, age):
        print("Création d'etre humain")
        self.nom = nom
        self._age = age
        
    def _getage(self):
        return self._age
    
    def _setage(self, nouvel_age):
        if (nouvel_age < 0):
            self._age = 0 
        else:
            self._age = nouvel_age
   
    # Property (<getter>, <setter>, <deleter>, <helper>)
    age = property(_getage, _setage)


# Programme principal

h1 = Humain("Jason" , 25)

print(h1._age)
h1.age = -5
print(h1._age)
        