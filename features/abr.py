from models.patient import Patient

class NoeudABR:
    def __init__(self, patient):
        self.patient = patient
        self.gauche = None
        self.droite = None

class ABR:
    def __init__(self):
        self.racine = None

    def ajouter_patient(self, patient):
        def _ajouter(noeud, patient):
            if not noeud:
                return NoeudABR(patient)
            if patient.id_patient < noeud.patient.id_patient:
                noeud.gauche = _ajouter(noeud.gauche, patient)
            else:
                noeud.droite = _ajouter(noeud.droite, patient)
            return noeud
        
        self.racine = _ajouter(self.racine, patient)

    def rechercher_patient(self, id_patient):
        def _rechercher(noeud, id_patient):
            if not noeud or noeud.patient.id_patient == id_patient:
                return noeud.patient if noeud else None
            if id_patient < noeud.patient.id_patient:
                return _rechercher(noeud.gauche, id_patient)
            return _rechercher(noeud.droite, id_patient)
        
        return _rechercher(self.racine, id_patient)

    def obtenir_tous_les_patients(self):
        def _inorder(noeud, patients):
            if noeud:
                _inorder(noeud.gauche, patients)
                patients.append(noeud.patient)
                _inorder(noeud.droite, patients)
        
        patients = []
        _inorder(self.racine, patients)
        return patients

    def supprimer_patient(self, id_patient):
        def _supprimer(noeud, id_patient):
            if not noeud:
                return None
            if id_patient < noeud.patient.id_patient:
                noeud.gauche = _supprimer(noeud.gauche, id_patient)
            elif id_patient > noeud.patient.id_patient:
                noeud.droite = _supprimer(noeud.droite, id_patient)
            else:
                if not noeud.gauche:
                    return noeud.droite
                if not noeud.droite:
                    return noeud.gauche
                successeur = noeud.droite
                while successeur.gauche:
                    successeur = successeur.gauche
                noeud.patient = successeur.patient
                noeud.droite = _supprimer(noeud.droite, successeur.patient.id_patient)
            return noeud
        
        self.racine = _supprimer(self.racine, id_patient)