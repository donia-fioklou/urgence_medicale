class Consultation:
    def __init__(self, date, medecin, diagnostic, traitement):
        self.date = date
        self.medecin = medecin
        self.diagnostic = diagnostic
        self.traitement = traitement
        self.suivant = None  # Liste chaînée

    def __str__(self):
        return f"{self.date} | Dr {self.medecin} | {self.diagnostic} | {self.traitement}"
