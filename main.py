from features.abr import ABR
from features.file_priorite import FilePriorite
from models.patient import Patient

# Initialisation des structures
tree = ABR()
file_priorite = FilePriorite()

def menu_principal():
    while True:
        print("\nMenu Principal")
        print("1. Gestion des Patients")
        print("2. Gestion des Urgences")
        print("3. Gestion de l'Historique Médical")
        print("4. Quitter")
        choix = input("Choix: ")
        if choix == "1":
            menu_patients()
        elif choix == "2":
            menu_urgences()
        elif choix == "3":
            menu_historique()
        elif choix == "4":
            break

def menu_patients():
    while True:
        print("\nGestion des Patients")
        print("1. Ajouter un patient")
        print("2. Rechercher un patient")
        print("3. Supprimer un patient")
        print("4. Voir la liste des patients")
        print("5. Retour")
        choix = input("Choix: ")
        if choix == "1":
            id_patient = input("ID: ")
            nom = input("Nom: ")
            age = int(input("Âge: "))
            pathologie = input("Pathologie: ")
            urgence = int(input("Niveau d'urgence: "))
            patient = Patient(id_patient, nom, age, pathologie, urgence)
            tree.ajouter_patient(patient)
            file_priorite.ajouter(patient)
            print("Patient ajouté avec succès.")
        elif choix == "2":
            id_patient = input("ID du patient: ")
            patient = tree.rechercher_patient(id_patient)
            print(patient if patient else "Patient non trouvé.")
        elif choix == "3":
            id_patient = input("ID du patient à supprimer: ")
            tree.supprimer_patient(id_patient)
            print("Patient supprimé.")
        elif choix == "4":
            patients = tree.obtenir_tous_les_patients()
            for p in patients:
                print(p)
        elif choix == "5":
            break

def menu_urgences():
    while True:
        print("\nGestion des Urgences")
        print("1. Modifier priorité")
        print("2. Extraire patient urgent")
        print("3. Voir la liste des urgences")
        print("4. Retour")
        choix = input("Choix: ")
        if choix == "1":
            id_patient = input("ID du patient: ")
            nouvelle_priorite = int(input("Nouvelle priorité: "))
            file_priorite.modifier_priorite(id_patient, nouvelle_priorite)
            print("Priorité modifiée.")
        elif choix == "2":
            patient = file_priorite.extraire()
            print(f"Patient prioritaire traité: {patient}")
        elif choix == "3":
            urgences = file_priorite.afficher_file()
            for p in urgences:
                print(p)
        elif choix == "4":
            break

def menu_historique():
    while True:
        print("\nGestion de l'Historique Médical")
        print("1. Ajouter une consultation")
        print("2. Voir l'historique d'un patient")
        print("3. Retour")
        choix = input("Choix: ")
        
        if choix == "1":
            id_patient = input("ID du patient: ")
            patient = tree.rechercher_patient(id_patient)
            if patient:
                date = input("Date de consultation (JJ/MM/AAAA) : ")
                medecin = input("Nom du médecin: ")
                diagnostic = input("Diagnostic: ")
                traitement = input("Traitement: ")
                patient.historique.ajouter_consultation(date, medecin, diagnostic, traitement)
                print("Consultation ajoutée avec succès.")
            else:
                print("Patient non trouvé.")
        
        elif choix == "2":
            id_patient = input("ID du patient: ")
            patient = tree.rechercher_patient(id_patient)
            if patient:
                print(f"\nHistorique médical de {patient.nom} :")
                patient.historique.afficher_historique()
            else:
                print("Patient non trouvé.")
        
        elif choix == "3":
            break


menu_principal()