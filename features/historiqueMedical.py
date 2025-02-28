

from models.consultation import Consultation


class HistoriqueMedical:
    def __init__(self):
        self.tete = None
    
    def ajouter_consultation(self, date, medecin, diagnostic, traitement):
        nouvelle_consultation = Consultation(date, medecin, diagnostic, traitement)
        if not self.tete:
            self.tete = nouvelle_consultation
        else:
            courant = self.tete
            while courant.suivant:
                courant = courant.suivant
            courant.suivant = nouvelle_consultation
    
    def afficher_historique(self):
        courant = self.tete
        while courant:
            print(f"Date: {courant.date}, Médecin: {courant.medecin}, Diagnostic: {courant.diagnostic}, Traitement: {courant.traitement}")
            courant = courant.suivant
