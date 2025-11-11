# 📘 Documentation complète du projet `Automat_Request`

## 🧾 Présentation générale

Le script **`fetch_users.py`** a pour objectif de :
- Récupérer des données d'utilisateurs depuis une API publique.  
- Extraire certaines informations pertinentes.  
- Générer un **fichier CSV** de rapport.  
- Afficher un résumé clair dans la console.  
- Gérer proprement les erreurs les plus courantes (réseau, données, écriture de fichier).

Ce document explique le **fonctionnement ligne par ligne** du script et détaille les **cas d’erreurs gérés**.

---

## 🧩 1️⃣ Importation des bibliothèques

```python
import requests
import csv
````

### Explication :

* `requests` : bibliothèque externe utilisée pour effectuer des requêtes HTTP (GET, POST, etc.) de manière simple et lisible.
* `csv` : module intégré à Python qui permet de lire et d’écrire des fichiers CSV.

> ⚠️ **Note :** le module `requests` doit être installé manuellement avec `pip install requests`.

---

## 🧩 2️⃣ Définition de la fonction principale

```python
def main():
```

* Le code principal du script est encapsulé dans une fonction `main()` pour améliorer la lisibilité et permettre une exécution propre via `if __name__ == "__main__":`.
* Cela évite que le code s’exécute automatiquement si le fichier est importé dans un autre script.

---

## 🧩 3️⃣ Étape 1 — Récupération des données depuis l’API

```python
try:
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    response.raise_for_status()
    users = response.json()
except requests.exceptions.RequestException as e:
    print("❌ Erreur lors de la requête API :", e)
    return
except ValueError:
    print("❌ Erreur : la réponse n’est pas un JSON valide.")
    return
```

### Explication ligne par ligne :

* `requests.get(url)` → envoie une requête HTTP **GET** à l’API.
* `response.raise_for_status()` → lève une erreur si le code HTTP n’est **pas 200** (par ex. 404, 500…).
* `response.json()` → convertit le contenu JSON de la réponse en **liste de dictionnaires Python**.

### Cas d’erreurs possibles :

1. **Erreur de réseau** → coupure Internet, serveur inaccessible.
   Exemple de message :

   ```
   ❌ Erreur lors de la requête API : HTTPSConnectionPool(...): Max retries exceeded
   ```

2. **Erreur HTTP** → si l’API renvoie un code différent de 200.
   Exemple :

   ```
   ❌ Erreur lors de la requête API : 404 Client Error
   ```

3. **Réponse non JSON** → si l’API renvoie un texte ou HTML au lieu de JSON.
   Message :

   ```
   ❌ Erreur : la réponse n’est pas un JSON valide.
   ```

---

## 🧩 4️⃣ Étape 2 — Extraction des champs nécessaires

```python
data = []
for user in users:
    data.append({
        "Name": user.get("name"),
        "Username": user.get("username"),
        "Email": user.get("email"),
        "Company": user.get("company", {}).get("name")
    })
```

### Explication ligne par ligne :

* `data = []` → crée une liste vide qui contiendra les informations nettoyées.
* `for user in users:` → boucle sur chaque utilisateur du JSON reçu.
* `user.get("name")` → récupère le champ `"name"` ; `.get()` évite les erreurs si la clé n’existe pas.
* `user.get("company", {}).get("name")` → récupère le nom de la compagnie en évitant une erreur si `"company"` est absent (grâce au `{}` par défaut).
* `append({...})` → ajoute un dictionnaire formaté à la liste `data`.

### Exemple de donnée générée :

```python
{
  "Name": "Leanne Graham",
  "Username": "Bret",
  "Email": "Sincere@april.biz",
  "Company": "Romaguera-Crona"
}
```

---

## 🧩 5️⃣ Étape 3 — Écriture du fichier CSV

```python
try:
    with open("users_report.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Name", "Username", "Email", "Company"])
        writer.writeheader()
        writer.writerows(data)
    print("✅ Fichier 'users_report.csv' créé avec succès.")
except IOError:
    print("❌ Erreur : impossible d’écrire dans le fichier CSV.")
    return
```

### Explication :

* `open("users_report.csv", "w", newline="", encoding="utf-8")` → ouvre le fichier en **écriture** (`"w"`) avec encodage UTF-8.

  * `newline=""` évite les lignes vides supplémentaires sous Windows.
* `csv.DictWriter()` → crée un objet permettant d’écrire des **dictionnaires** directement dans un fichier CSV.
* `writer.writeheader()` → écrit la ligne d’en-tête : `Name,Username,Email,Company`.
* `writer.writerows(data)` → écrit chaque dictionnaire de `data` sous forme de ligne CSV.

### Cas d’erreurs possibles :

1. **Erreur d’écriture** (ex. permissions, disque plein, fichier ouvert ailleurs).
   Message :

   ```
   ❌ Erreur : impossible d’écrire dans le fichier CSV.
   ```

2. **Erreur d’encodage** (rare, si des caractères spéciaux non pris en charge apparaissent).

---

## 🧩 6️⃣ Étape 4 — Affichage du résumé dans la console

```python
total_users = len(data)
companies = sorted(set([user["Company"] for user in data if user["Company"]]))
print(f"📊 Total users: {total_users} | Companies: {companies}")
```

### Explication :

* `len(data)` → compte le nombre total d’utilisateurs traités.
* `[user["Company"] for user in data if user["Company"]]` → crée une liste contenant uniquement les noms d’entreprises non vides.
* `set(...)` → supprime les doublons.
* `sorted(...)` → trie la liste de sociétés par ordre alphabétique.
* `print(...)` → affiche le résumé final au format :

  ```
  📊 Total users: 10 | Companies: ['Deckow-Crist', 'Romaguera-Crona', ...]
  ```

---

## 🧩 7️⃣ Point d’entrée du script

```python
if __name__ == "__main__":
    main()
```

### Explication :

* Cette condition vérifie si le script est exécuté **directement** (et non importé).
* Si c’est le cas, la fonction `main()` est appelée.
* Cela permet de réutiliser ce code dans d’autres modules sans qu’il ne s’exécute automatiquement.

---

## 🧠 Récapitulatif du flux d’exécution

1. Le script démarre par `main()`.
2. Il récupère les utilisateurs depuis l’API (`GET /users`).
3. Il extrait les champs utiles et les stocke dans `data`.
4. Il écrit les données dans un fichier CSV.
5. Il affiche un résumé dans la console.
6. En cas de problème, une erreur claire est affichée et le script s’arrête proprement.

---

## ⚠️ Gestion des erreurs (récapitulatif)

| Type d’erreur      | Cause probable                        | Message affiché                                    |
| ------------------ | ------------------------------------- | -------------------------------------------------- |
| `RequestException` | API inaccessible / pas d’Internet     | ❌ Erreur lors de la requête API                    |
| `ValueError`       | Réponse non JSON                      | ❌ Erreur : la réponse n’est pas un JSON valide     |
| `IOError`          | Fichier CSV verrouillé / disque plein | ❌ Erreur : impossible d’écrire dans le fichier CSV |

---

## 🧩 Exemple de sortie complète dans la console

```
✅ Fichier 'users_report.csv' créé avec succès.
📊 Total users: 10 | Companies: ['Deckow-Crist', 'Romaguera-Crona', 'Romaguera-Jacobson', 'Romaguera-Kilback']
```

---

## 🧰 Bonnes pratiques appliquées

* **Encapsulation** dans une fonction `main()` pour éviter l’exécution accidentelle.
* **Utilisation de `.get()`** pour éviter les erreurs de clé manquante.
* **Tri et déduplication** des entreprises avec `set()` et `sorted()`.
* **Gestion des erreurs** avec des messages clairs pour chaque étape critique.
* **Encodage UTF-8** pour compatibilité internationale.

---

## 🧪 Conseils de test

1. **Test normal :**

   ```bash
   python fetch_users.py
   ```

   → Doit créer `users_report.csv` et afficher les résultats.

2. **Test sans Internet :**
   → Couper la connexion réseau pour voir le message d’erreur d’API.

3. **Test URL invalide :**
   → Modifier la ligne `requests.get(...)` avec une mauvaise URL :

   ```python
   response = requests.get("https://jsonplaceholder.typicode.com/userx")
   ```

   → Le script renverra une erreur 404.

4. **Test de fichier protégé :**
   → Ouvrir `users_report.csv` dans Excel sans le fermer et relancer le script.

---

## 📦 Résumé technique

| Élément          | Description                                  |
| ---------------- | -------------------------------------------- |
| Langage          | Python 3.x                                   |
| Dépendances      | `requests`                                   |
| Modules intégrés | `csv`                                        |
| API utilisée     | `https://jsonplaceholder.typicode.com/users` |
| Fichier généré   | `users_report.csv`                           |
| Format de sortie | CSV + résumé console                         |

---

## 🧑‍💻 Auteur

Projet développé par **Halid13**