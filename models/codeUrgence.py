import tkinter as tk
from tkinter import ttk
def afficher_Patient(filtre=""):
    for row in tree_Patient.get_children():
        tree_Patient.delete(row)
    patients = tree.obtenir_tous_les_patients()
    for p in patients:
        if filtre.lower() in p.nom.lower():  # Filtrage insensible à la casse
          tree_Patient.insert("", tk.END, values=(p.id_patient,p.nom,p.age+" An(s)",p.pathologie,p.urgence))