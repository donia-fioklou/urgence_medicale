class FilePriorite:
    def __init__(self):
        self.patients = []

    def ajouter(self, patient):
        self.patients.append(patient)
        self._monter(len(self.patients) - 1)

    def _monter(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.patients[index].urgence < self.patients[parent].urgence:
                self.patients[index], self.patients[parent] = self.patients[parent], self.patients[index]
                index = parent
            else:
                break

    def extraire(self):
        if not self.patients:
            return None
        if len(self.patients) == 1:
            return self.patients.pop(0)
        top = self.patients[0]
        self.patients[0] = self.patients.pop()
        self._descendre(0)
        return top

    def _descendre(self, index):
        taille = len(self.patients)
        while True:
            gauche = 2 * index + 1
            droite = 2 * index + 2
            plus_petit = index

            if gauche < taille and self.patients[gauche].urgence < self.patients[plus_petit].urgence:
                plus_petit = gauche
            if droite < taille and self.patients[droite].urgence < self.patients[plus_petit].urgence:
                plus_petit = droite
            if plus_petit == index:
                break

            self.patients[index], self.patients[plus_petit] = self.patients[plus_petit], self.patients[index]
            index = plus_petit

    def modifier_priorite(self, id_patient, nouvelle_priorite):
        for i, patient in enumerate(self.patients):
            if patient.id_patient == id_patient:
                patient.urgence = nouvelle_priorite
                self._monter(i)
                self._descendre(i)
                return 1
                break
    def verifier_patient(self, id_patient):
        for i, patient in enumerate(self.patients):
            if patient.id_patient == id_patient:
              return 1
               

    def afficher_file(self):
        return self.patients
        #return [str(p) for p in self.patients]
