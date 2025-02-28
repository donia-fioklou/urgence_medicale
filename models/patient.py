from features.historiqueMedical import HistoriqueMedical

class Patient:
    def __init__(self, id_patient, nom, age, pathologie, urgence):
        self.id_patient = id_patient
        self.nom = nom
        self.age = age
        self.pathologie = pathologie
        self.urgence = urgence
        self.historique = HistoriqueMedical()  # Historique médical du patient

    def __str__(self):
        return f"{self.id_patient} - {self.nom}, {self.age} ans, {self.pathologie}, Urgence: {self.urgence}"
