class Voiture:
    def __init__(self,matricule, marque, couleur):
        self.matricule = matricule
        self.marque = marque
        self.couleur = couleur
    def afficherinformations(self):
        print(f"Matricule : {self.matricule}")
        print(f".Marque : {self.marque}")
        print(f"Couleur : {self.couleur}")

class Parc :
    def __init__(self):
        self.id_parc = id_parc
        self.adresse = adresse
        self.capacite = capacite
        self.liste_voiture = []

