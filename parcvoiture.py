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
