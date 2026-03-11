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
    def entrerVoiture(self, voiture):
        if len(voiture.liste_voiture) >= self.capacite:
            print("parc plein")
            return
        for v in self.liste_voiture:
            if v.matricule == voiture.matricule:
                print("la voiture est deja dans le parc")
                return
        self.liste_voiture.append(voiture)
        print("voiture ajouter aux parc")
    def sortirVoiture(self, matricule):
        for v in self.liste_voiture:
            if v.matricule == matricule:
                self.liste_voiture.remove(v)
                print("voiture sortir")
                return
        print("voiture non pas dans le parc")
    def calculeNbrPlacesLibres(self):
        return self.capacite - len(self.liste_voiture)
parc = Parc(777, "parc Boreal", 3)
v1= Voiture("T0121", "Mercedes", "Argent")
v2= Voiture("T0122", "Volkswagen", "Bleu")
v3= Voiture("T0123", "Chevrolet", "rouge")

