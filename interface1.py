import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import Font

from features.abr import ABR
from PIL import Image, ImageTk


import pickle



from features.file_priorite import FilePriorite
from models.patient import Patient
# Initialisation des structures
tree = ABR()

file_priorite = FilePriorite()
# Déclaration des champs de saisie comme variables globales
global entry_Urgence,entry_Age,entry_Id,entry_Nom,entry_Patologie
global entry_Id_Urgence,entry_nom_Urgence
global entry_trai,entry_dia,entry_nom_medecin,entry_date,entry_Id_h,entry_rechercher
# Fonctions pour vider les chant de saisi
def vider_champs():
    # Champs pour les Patient
    entry_Id.delete(0, tk.END)
    entry_Nom.delete(0, tk.END)
    entry_Age.delete(0, tk.END)
    entry_Patologie.delete(0, tk.END)
    entry_Urgence.delete(0, tk.END)
    entry_trai.delete(0, tk.END)
    entry_dia.delete(0, tk.END)
    entry_nom_medecin.delete(0, tk.END)
    entry_date.delete(0, tk.END)
    entry_Id_h.delete(0, tk.END) 
    entry_Id_Urgence.delete(0, tk.END)
    entry_nom_Urgence.delete(0, tk.END)

# Sauvegarder les données dans un fichier
def sauvegarder_donnees():
    with open('donnees.pkl', 'wb') as fichier:
        # Sérialisation des objets
        pickle.dump(tree, fichier)
        pickle.dump(file_priorite, fichier)
       # messagebox.showinfo("Sauvegarde", "Les données ont été sauvegardées avec succès.")

# Charger les données depuis le fichier
def charger_donnees():
    try:
        with open('donnees.pkl', 'rb') as fichier:
            # Désérialisation des objets
            global tree
            global file_priorite
            tree = pickle.load(fichier)
            file_priorite = pickle.load(fichier)
            #messagebox.showinfo("Chargement", "Les données ont été chargées avec succès.")
    except FileNotFoundError:
        messagebox.showwarning("Aucun fichier", "Aucune sauvegarde précédente trouvée.")


## AFFICHER PATIENT
def afficher_Patient(filtre=""):
    for row in tree_Patient.get_children():
        tree_Patient.delete(row)
    patients = tree.obtenir_tous_les_patients()
    for p in patients:
        if filtre.lower() in p.id_patient.lower():  # Filtrage insensible à la casse
          tree_Patient.insert("", tk.END, values=(p.id_patient,p.nom,f"{p.age} An(s)",p.pathologie,p.urgence))

# Fonction qui sera appelée lors de la saisie dans le champ de recherche
def mise_a_jour_recherche(event):
    filtre = entry_rechercher_Patient.get()
    afficher_Patient(filtre)

def supprimer_Patient():
    selected_item = tree_Patient.selection()
    if selected_item:
        id = tree_Patient.item(selected_item, "values")[0]
        tree. supprimer_patient(id)
        
        afficher_Patient()
        afficher_urgence
        vider_champs()
        messagebox.showwarning("", "Patient supprimé avec succès !")
       
    else:
        messagebox.showwarning("Erreur", "Veuillez sélectionner le patient à supprimer.")


def ajouter_patient():
    id = entry_Id.get()
    nom = entry_Nom.get()
    patologie = entry_Patologie.get()
    
    # Vérifier que l'âge et la priorité ne sont pas vides avant de tenter la conversion
    age_str = entry_Age.get().strip()
    urgence_str = entry_Urgence.get().strip()

    if not age_str or not urgence_str:
        messagebox.showwarning("Erreur", "L'âge et la priorité ne peuvent pas être vides.")
        return

    try:
        # Essayer de convertir l'âge et la priorité en entiers
        age = int(age_str)
        urgence = int(urgence_str)
        t=file_priorite.verifier_patient(id)

        # Si tous les champs sont remplis, on ajoute le patient
        if id and nom and age and patologie and urgence:
            if (t):
                 messagebox.showinfo("","Id existe déja")
            else :   
                patient = Patient(id, nom, age, patologie, urgence)
                tree.ajouter_patient(patient)
                file_priorite.ajouter(patient)
                afficher_Patient()
                afficher_urgence()
                vider_champs()
                sauvegarder_donnees()
                messagebox.showinfo("","Patient ajouté avec succès !")
        else:
            messagebox.showwarning("Erreur", "Tous les champs doivent être remplis.")
        
    except ValueError:
        # Si une erreur se produit lors de la conversion en entier
        messagebox.showwarning("Erreur", "L'âge et la priorité doivent être des entiers.")
    
    # Vider les champs après ajout
   



                        ### Urgence

"""def afficher_urgence(filtre=""):
    for row in tree_urgence.get_children():
        tree_urgence.delete(row)
    patients = tree.obtenir_tous_les_patients()
    for p in patients:
        if filtre.lower() in p.nom.lower():  # Filtrage insensible à la casse
          tree_urgence.insert("", tk.END, values=(p.id_patient,p.nom,f"{p.age} An(s)",p.pathologie,p.urgence))"""
def afficher_urgence():
    for row in tree_urgence.get_children():
        tree_urgence.delete(row)

    urgence_ = file_priorite.afficher_file()
    for p in urgence_:
        tree_urgence.insert("", tk.END, values=(p.id_patient,p.nom,f"{p.age} An(s)",p.pathologie,p.urgence))

## modifier proirité
def modifier_prio():
    t=0
     
    idt = entry_Id_Urgence.get().strip()
    nomt= entry_nom_Urgence.get().strip()
    if not idt or not nomt:
        messagebox.showwarning("Erreur", "Champs vides.")
        return
    try:
        id=idt
        nom=int(nomt)
        t=file_priorite.modifier_priorite(id,nom)
        if(t):
            messagebox.showwarning("","Priorité modifiée.")
            vider_champs()
            
        else:  messagebox.showwarning("Erreur","Id non trouvé.")
        
    except ValueError:
        # Si une erreur se produit lors de la conversion en entier
        messagebox.showwarning("Erreur", "La priorité doit être un entier.")
    afficher_urgence()
    afficher_Patient()

def extrairePatient():
     patient = file_priorite.extraire()
     messagebox.showwarning("",f"Patient prioritaire traité: {patient}")
     afficher_urgence()
     sauvegarder_donnees()
     
    # print(f"Patient prioritaire traité: {patient}")
def ajouter_consultation():
             
            id = entry_Id_h.get().strip()
            date=entry_date.get().strip()
            medecin=entry_nom_medecin.get().strip()
            diagnostic=entry_dia.get().strip()
            traitement=entry_trai.get().strip()
            if not id or not date or not medecin or not diagnostic or not traitement:
              messagebox.showwarning("Erreur", "Champs vides.")
              return
            patient = tree.rechercher_patient(id)

            if patient:
                
                patient.historique.ajouter_consultation(date, medecin, diagnostic, traitement)
                messagebox.showwarning("","Consultation ajoutée avec succès.")
                vider_champs()
                sauvegarder_donnees()
               
            else:
                messagebox.showwarning("","Patient non trouvé.")

def rechercher():
    
    for row in tree_historique.get_children():
        tree_historique.delete(row)
    id_patient = entry_rechercher.get()
    patient = tree.rechercher_patient(id_patient)
    if patient:
                print(f"\nHistorique médical de {patient.nom} :")
                date,medecin,diagn,traite=patient.historique.afficher_historique()
                tree_historique.insert("", tk.END, values=(patient.nom,date,medecin,diagn,traite))
                
    else:
               messagebox.showwarning("","Patient non trouvé.")
   # for p in urgence_:
      #  tree_urgence.insert("", tk.END, values=(p.id_patient,p.nom,f"{p.age} An(s)",p.pathologie,p.urgence))
       #  print(f"Date: {courant.date}, Médecin: {courant.medecin}, Diagnostic: {courant.diagnostic}, Traitement: {courant.traitement}
#menu_principal()
# Couleurs et polices
BACKGROUND_COLOR =  "#f0f0f0"
BUTTON_COLOR = "#f0f0f0"
TEXT_COLOR = "#333333"
FONT = ("Arial", 12)


root = tk.Tk()
root.title("Système de Gestion des Urgences Médicales")
root.geometry("1300x710")
## LOGO
logo_path = "logo.jpg" 
imageL = Image.open(logo_path)
imageL = imageL.resize((300, 300))  
logo = ImageTk.PhotoImage(imageL)

root.iconphoto(False, logo)
root.configure(bg=BACKGROUND_COLOR)
# Barre de statut
status_bar = ttk.Label(root, text="HOPITAL  ", relief=tk.SUNKEN, anchor=tk.W, )
status_bar.pack(side=tk.BOTTOM, fill=tk.X)
# Onglets
Med = ttk.Notebook(root)
Med.pack(fill="both", expand=True)

# Onglet Patient
tab_patient = ttk.Frame(Med)
Med.add(tab_patient, text="Gestion des Patients")

style = ttk.Style()
style.configure("TNotebook.Tab", font=("Arial", 12), padding=[10, 5])
style.map("TNotebook.Tab",
          #background=[("selected", "#4CAF50")],  # Couleur de fond lorsque l'onglet est sélectionné
          foreground=[("selected", "#4CAF50")]) 
# Champs de saisie pour ajouter un lpatient
#frame_ajouter_image = ttk.LabelFrame(tab_patient, text="Ajouter un Patient", padding=10)
#frame_ajouter_image.grid(row=1, column=5, padx=10, pady=10, sticky="ew")
# Charger une image
image_path = "im1.jpg"  # Remplacez par le chemin réel de votre image
image = Image.open(image_path)
image = image.resize((200, 200))  # Ajustez la taille de l'image si nécessaire
photo = ImageTk.PhotoImage(image)

# Créer un Label pour afficher l'image
label_image = ttk.Label(tab_patient, image=photo)
label_image.grid(row=0, column=2, padx=10, pady=10)  # Vous pouvez ajuster la position selon vos besoins

# Champs de saisie pour ajouter un lpatient
frame_ajouter_Patient = ttk.LabelFrame(tab_patient, text="Ajouter un Patient", padding=10)
frame_ajouter_Patient.grid(row=0, column=0, padx=10, pady=10, sticky="ew")



label_Id = ttk.Label(frame_ajouter_Patient, text="ID :")
label_Id.grid(row=0, column=0, padx=5, pady=5)
entry_Id = ttk.Entry(frame_ajouter_Patient)
entry_Id.grid(row=0, column=1, padx=5, pady=5)

label_Nom = ttk.Label(frame_ajouter_Patient, text="NOM :")
label_Nom.grid(row=1, column=0, padx=5, pady=5)
entry_Nom = ttk.Entry(frame_ajouter_Patient)
entry_Nom.grid(row=1, column=1, padx=5, pady=5)

label_Age= ttk.Label(frame_ajouter_Patient, text="AGE:")
label_Age.grid(row=2, column=0, padx=5, pady=5)
entry_Age = ttk.Entry(frame_ajouter_Patient)
entry_Age.grid(row=2, column=1, padx=5, pady=5)

label_Patologie = ttk.Label(frame_ajouter_Patient, text="PATHOLOGIE:")
label_Patologie.grid(row=3, column=0, padx=5, pady=5)
entry_Patologie = ttk.Entry(frame_ajouter_Patient)
entry_Patologie.grid(row=3, column=1, padx=5, pady=5)

label_Urgence = ttk.Label(frame_ajouter_Patient, text="URGENCE :")
label_Urgence.grid(row=4, column=0, padx=5, pady=5)
entry_Urgence = ttk.Entry(frame_ajouter_Patient)
entry_Urgence.grid(row=4, column=1, padx=5, pady=5)

button_ajouter_P = ttk.Button(frame_ajouter_Patient, text="Ajouter un Patient",command=ajouter_patient)
button_ajouter_P.grid(row=5, column=0, columnspan=2, pady=10)

#button_modifier_P = ttk.Button(frame_ajouter_Patient, text="Modifier un Patient")# command=modifier)
#button_modifier_P.grid(row=6, column=0, pady=10)

button_supprimer_P = ttk.Button(frame_ajouter_Patient, text="Supprimer un Patient", command=supprimer_Patient)
button_supprimer_P.grid(row=6, column=0, columnspan=2,pady=10)

# Champ de saisie pour rechercher un Patient
frame_rechercher_Patient = ttk.LabelFrame(tab_patient, text="Rechercher un Patient", padding=10)
frame_rechercher_Patient.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

label_rechercher_Patient = ttk.Label(frame_rechercher_Patient, text="Rechercher par ID :")
label_rechercher_Patient.grid(row=0, column=0, padx=5, pady=5)
entry_rechercher_Patient = ttk.Entry(frame_rechercher_Patient)
entry_rechercher_Patient.grid(row=0, column=1, padx=5, pady=5)

# Lier la fonction mise_a_jour_recherche à l'événement de saisie dans le champ de recherche
entry_rechercher_Patient.bind("<KeyRelease>", mise_a_jour_recherche)

# Tableau pour afficher les Patients
frame_tableau_patient = ttk.LabelFrame(tab_patient, text="Liste des Patients", padding=10)
frame_tableau_patient.grid(row=2, column=0, padx=10, pady=0, sticky="nsew")

columns = ("Id", "Nom","Age", "Pathologie", "Urgende_Niveau")
tree_Patient = ttk.Treeview(frame_tableau_patient, columns=columns, show="headings", selectmode="browse")
tree_Patient.heading("Id", text="Id")
tree_Patient.heading("Nom", text="Nom")
tree_Patient.heading("Age", text="Age")
tree_Patient.heading("Pathologie", text="Pathologie")
tree_Patient.heading("Urgende_Niveau", text="Niveau d'Urgence")

tree_Patient.pack(fill="both", expand=True)




#URGENCE
tab_Urgence = ttk.Frame(Med)
Med.add(tab_Urgence,text="Gestion des Urgences")

label_image = ttk.Label(tab_Urgence, image=photo)
label_image.grid(row=0, column=2, padx=10, pady=10)


# Champs de saisie pour modifier l'etat d'urgence 
frame_urgence = ttk.LabelFrame(tab_Urgence, text="Modifier Priorité", padding=10)
frame_urgence.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

label_Id_urgence = ttk.Label(frame_urgence, text="ID Patient:")
label_Id_urgence.grid(row=0, column=0, padx=5, pady=5)
entry_Id_Urgence = ttk.Entry(frame_urgence)
entry_Id_Urgence.grid(row=0, column=1, padx=5, pady=5)

label_i_urgence = ttk.Label(frame_urgence, text="Urgence:")
label_i_urgence.grid(row=1, column=0, padx=5, pady=5)
entry_nom_Urgence = ttk.Entry(frame_urgence)
entry_nom_Urgence.grid(row=1, column=1, padx=5, pady=5)

button_modifier_prio = ttk.Button(frame_urgence, text="Modifier Urgence",command=modifier_prio)
button_modifier_prio.grid(row=5, column=0, columnspan=2, pady=10)

button_extraire = ttk.Button(frame_urgence, text="Extraire Patient",command=extrairePatient)
button_extraire.grid(row=8, column=0, columnspan=2, pady=10)

# Id urgence
frame_tableau_urgence = ttk.LabelFrame(tab_Urgence, text="Liste des Urgnces", padding=10)
frame_tableau_urgence.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

column = ("Id", "Nom","Age", "Pathologie", "Urgende_Niveau")
tree_urgence = ttk.Treeview(frame_tableau_urgence, columns=column, show="headings", selectmode="browse")
tree_urgence.heading("Id", text="Id")
tree_urgence.heading("Nom", text="Nom")
tree_urgence.heading("Age", text="Age")
tree_urgence.heading("Pathologie", text="Pathologie")
tree_urgence.heading("Urgende_Niveau", text="Niveau d'Urgence")

tree_urgence.pack(fill="both", expand=True)
#afficher_urgence(tab_Urgence, tree)

# Onglet Historique
tab_historique = ttk.Frame(Med)
Med.add(tab_historique, text="Gestion de l'Historique Médical")

label_image = ttk.Label(tab_historique, image=photo)
label_image.grid(row=0, column=2, padx=10, pady=10)

# Champs de saisie pour ajouter un livre
frame_historique = ttk.LabelFrame(tab_historique, text="HISTORIQUE", padding=10)
frame_historique.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

label_Id_h = ttk.Label(frame_historique, text="ID Patient:")
label_Id_h.grid(row=0, column=0, padx=5, pady=5)
entry_Id_h= ttk.Entry(frame_historique)
entry_Id_h.grid(row=0, column=1, padx=5, pady=5)

label_date = ttk.Label(frame_historique, text="Date de Consultation :")
label_date.grid(row=1, column=0, padx=5, pady=5)
entry_date = ttk.Entry(frame_historique)
entry_date.grid(row=1, column=1, padx=5, pady=5)

label_nom_h= ttk.Label(frame_historique, text="Nom de Medecin:")
label_nom_h.grid(row=2, column=0, padx=5, pady=5)
entry_nom_medecin = ttk.Entry(frame_historique)
entry_nom_medecin.grid(row=2, column=1, padx=5, pady=5)

label_dia = ttk.Label(frame_historique, text="Diagnostic:")
label_dia.grid(row=3, column=0, padx=5, pady=5)
entry_dia = ttk.Entry(frame_historique)
entry_dia.grid(row=3, column=1, padx=5, pady=5)

label_trai = ttk.Label(frame_historique, text="Traitement:")
label_trai.grid(row=4, column=0, padx=5, pady=5)
entry_trai = ttk.Entry(frame_historique)
entry_trai.grid(row=4, column=1, padx=5, pady=5)

button_ajouter_livre = ttk.Button(frame_historique, text="Ajouter un Patient",command=ajouter_consultation)
button_ajouter_livre.grid(row=5, column=0, columnspan=2, pady=10)

frame_rechercher = ttk.LabelFrame(tab_historique, text="Rechercher un Patient", padding=10)
frame_rechercher.grid(row=7, column=0, padx=10, pady=10, sticky="ew")

label_rechercher = ttk.Label(frame_rechercher, text="Rechercher par ID :")
label_rechercher.grid(row=8, column=0, padx=5, pady=5)
entry_rechercher = ttk.Entry(frame_rechercher)
entry_rechercher.grid(row=8, column=1, padx=5, pady=5)
button_ajouterH= ttk.Button(frame_rechercher, text="valider",command=rechercher)
button_ajouterH.grid(row=9, column=1, columnspan=2, pady=10)

###Tableau historique
frame_tableau_historique = ttk.LabelFrame(tab_historique, text="Historique Medicale", padding=10)
frame_tableau_historique.grid(row=8, column=0, padx=10, pady=10, sticky="nsew")

column = ("Id", "Date","Medecin", "Diagnostic", "Traitement")
tree_historique = ttk.Treeview(frame_tableau_historique, columns=column, show="headings", selectmode="browse")
tree_historique.heading("Id", text="Patient")
tree_historique.heading("Date", text="Date")
tree_historique.heading("Medecin", text="Medecin")
tree_historique.heading("Diagnostic", text="Diagnostic")
tree_historique.heading("Traitement", text="Traitement")

tree_historique.pack(fill="both", expand=True)



charger_donnees()
afficher_urgence()
afficher_Patient()

root.mainloop()
