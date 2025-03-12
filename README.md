
# 🚑 **Système de Gestion des Urgences Médicales**  

Ce projet est une application CLI permettant de gérer les patients, les urgences et l'historique médical à l'aide de structures de données avancées (**Arbre Binaire de Recherche, File de Priorité et Liste Chaînée**).  

## 📌 **Fonctionnalités**  
✅ **Gestion des Patients** : Ajout, recherche, suppression et affichage des patients.  
✅ **Gestion des Urgences** : Priorisation et extraction des patients en situation d’urgence.  
✅ **Gestion de l’Historique Médical** : Enregistrement et consultation des consultations des patients.  

---

## 📂 **Architecture du Projet**  
```
urgence_medicale/
│── models/
│   ├── patient.py        # Classe Patient
│   ├── consultation.py   # Classe Consultation
│── features/
│   ├── abr.py            # Arbre Binaire de Recherche pour gérer les patients
│   ├── file_priorite.py  # File de Priorité pour la gestion des urgences
|   ├── historiqueMedical.py # Gestion de l'historique médical (Liste Chaînée)
│── main.py               # Interface CLI du projet
│── README.md             # Documentation du projet
```

---

## 🚀 **Installation & Exécution**  

### **1️⃣ Cloner le projet**  
```bash
git clone https://github.com/donia-fioklou/urgence_medicale.git
cd urgence_medicale
```

### **2️⃣ Installer Python (si ce n'est pas déjà fait)**  
Ce projet fonctionne avec **Python 3.7+**. Vérifiez votre version avec :  
```bash
python --version
pip install pillow
```

### **3️⃣ Lancer l'application**  
Exécute simplement :  
```bash
python urgence_medicale/interface1.py
```

---

## ⚙️ **Utilisation**  

Le menu principal propose trois sections principales :  

1️⃣ **Gestion des Patients**  
   - Ajouter un patient  
   - Rechercher un patient  
   - Supprimer un patient  
   - Voir la liste des patients  

2️⃣ **Gestion des Urgences**  
   - Modifier la priorité d’un patient  
   - Extraire le patient le plus urgent  
   - Voir la liste des urgences  

3️⃣ **Gestion de l’Historique Médical**  
   - Ajouter une consultation à un patient  
   - Consulter l’historique médical d’un patient  

---

## 🛠 **Technologies utilisées**  
- **Python 3**  
- **Structures de données avancées** :  
  - **Arbre Binaire de Recherche (ABR)** pour la gestion des patients  
  - **File de Priorité** pour la gestion des urgences  
  - **Liste Chaînée** pour l'historique médical  
-pickle "pour sauvegarder les objets"

---
