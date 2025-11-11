# 🧾 Automat_Request - fetch_users.py

## 📘 Description du projet
Ce projet contient un script Python nommé **`fetch_users.py`** qui récupère des données d'utilisateurs depuis une **API publique**, les traite, et génère un **rapport CSV**.  
Il s'agit d'un exercice typique d'automatisation qu'un ingénieur IT ou un développeur pourrait rencontrer, par exemple pour intégrer ou analyser des données externes.


## 🚀 Fonctionnalités

Le script réalise les actions suivantes :

1. **Récupère les utilisateurs** depuis l’API publique :  
   [`https://jsonplaceholder.typicode.com/users`](https://jsonplaceholder.typicode.com/users)

2. **Extrait les informations suivantes** pour chaque utilisateur :  
   - `name`  
   - `username`  
   - `email`  
   - `company.name`

3. **Enregistre les données** dans un fichier CSV nommé **`users_report.csv`** avec les colonnes :  
   `Name, Username, Email, Company`

4. **Affiche dans la console** :
   - le nombre total d’utilisateurs récupérés  
   - la liste **unique et triée** des noms d’entreprises  

5. **Gère les erreurs** possibles :
   - Problème de connexion ou d’accès à l’API  
   - Réponse JSON invalide  
   - Erreur lors de l’écriture du fichier CSV  


## 🧩 Exemple de sortie console

```bash
✅ Fichier 'users_report.csv' créé avec succès.
📊 Total users: 10 | Companies: ['Deckow-Crist', 'Romaguera-Crona', 'Romaguera-Jacobson', 'Romaguera-Jacobson', ...]
````


## 📄 Exemple de contenu du fichier `users_report.csv`

| Name          | Username  | Email                                         | Company         |
| ------------- | --------- | --------------------------------------------- | --------------- |
| Leanne Graham | Bret      | [Sincere@april.biz](mailto:Sincere@april.biz) | Romaguera-Crona |
| Ervin Howell  | Antonette | [Shanna@melissa.tv](mailto:Shanna@melissa.tv) | Deckow-Crist    |
| ...           | ...       | ...                                           | ...             |


## 🛠️ Exécution

### 1. Vérifier que Python est installé

```bash
python --version
```

ou

```bash
python3 --version
```

### 2. Installer les dépendances

```bash
pip install requests
```

ou

```bash
pip3 install requests
```

### 3. Exécuter le script

```bash
python fetch_users.py
```

ou

```bash
python3 fetch_users.py
```


## 🧠 Notes techniques

* Le script utilise la bibliothèque `requests` pour interroger l’API.
* Le module `csv` est utilisé pour générer le fichier `users_report.csv`.
* Le code gère proprement les erreurs d’exécution grâce à des blocs `try/except`.
* Les noms d’entreprises sont filtrés et triés pour éviter les doublons.

---

## 🧰 Technologies utilisées

* **Langage** : Python 3.x
* **Librairies** :

  * `requests`
  * `csv` (native à Python)


## 🧪 Tests manuels

Tu peux tester la gestion des erreurs en :

* Coupant ta connexion Internet pour simuler une erreur réseau.
* Changeant l’URL de l’API (`/userx` au lieu de `/users`) pour simuler une erreur HTTP 404.
* Rendant le fichier CSV en lecture seule pour tester une erreur d’écriture.


## 🧑‍💻 Auteur

Projet réalisé par **Halid13**
