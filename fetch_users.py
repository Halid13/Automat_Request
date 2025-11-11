import requests
import csv

def main():
    # Étape 1 — Requête à l’API
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        response.raise_for_status()  # Vérifie que la réponse est OK (code 200)
        users = response.json()  # Convertit la réponse JSON en liste Python
    except requests.exceptions.RequestException as e:
        print("❌ Erreur lors de la requête API :", e)
        return
    except ValueError:
        print("❌ Erreur : la réponse n’est pas un JSON valide.")
        return

    # Étape 2 — Extraction des champs nécessaires
    data = []
    for user in users:
        data.append({
            "Name": user.get("name"),
            "Username": user.get("username"),
            "Email": user.get("email"),
            "Company": user.get("company", {}).get("name")
        })

    # Étape 3 — Enregistrement dans un fichier CSV
    try:
        with open("users_report.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["Name", "Username", "Email", "Company"])
            writer.writeheader()
            writer.writerows(data)
        print("✅ Fichier 'users_report.csv' créé avec succès.")
    except IOError:
        print("❌ Erreur : impossible d’écrire dans le fichier CSV.")
        return

    # Étape 4 — Affichage du résumé
    total_users = len(data)
    companies = sorted(set([user["Company"] for user in data if user["Company"]]))
    print(f"📊 Total users: {total_users} | Companies: {companies}")

if __name__ == "__main__":
    main()
