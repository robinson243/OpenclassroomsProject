# Définition


class EtreVivant:
    espece_etre_vivant = "(etre vivan non identifié)"
    def AfficherInfosEtreVivant(self):
        print(f"Info etre vivant : " + self.espece_etre_vivant)

class Chat(EtreVivant):
    espece_etre_vivant = "Chat (Mammifère félin)"

class Personne(EtreVivant):
    espece_etre_vivant = "Humain (Mammifère Homo Sapiens)"
    
    def __init__(self, nom: str = "", age: int = 0):
        self.nom = nom
        self.age = age
        if nom == "":
            self.demanderNom()
        print("Connstructeur personne: " + nom)
        
    def sePresenter(self):
        info_personne = f"Bonjour je m'appelle {self.nom}"
        if self.age != 0:
            info_personne += f", j'ai {self.age} ans"
        print(info_personne)
        if self.age != 0:
            if self.estMajeur():
                print("Je suis majeur")
            else:
                print("Je suis mineur")
            
    def estMajeur(self):
        return self.age >= 18
    
    def demanderNom(self):
        self.nom = input("Votre nom > ")
    

# Utilisation

# personne1 = Personne("Jean", 30) # Je crée une personne
# personne2 = Personne("Paul", 15) # Je crée une personne

liste_personnes = [Personne("Jean", 30),Personne("Paul", 15), Personne("Zoé", 8)]
for p in liste_personnes:
    p.sePresenter()
    p.AfficherInfosEtreVivant()
    print()
    
    
chat = Chat()
chat.AfficherInfosEtreVivant()
