class Voiture:
    def __init__(self,matricule, marque, couleur):
        self.matricule = matricule
        self.marque = marque
        self.couleur = couleur
    def afficherinformations(self):
        print(self.matricule)
        print(self.marque)
        print(self.couleur)
