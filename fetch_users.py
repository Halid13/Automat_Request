import requests
import csv

def main():
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

    data = []
    for user in users:
        data.append({
            "Name": user.get("name"),
            "Username": user.get("username"),
            "Email": user.get("email"),
            "Company": user.get("company", {}).get("name")
        })

    try:
        with open("users_report.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["Name", "Username", "Email", "Company"])
            writer.writeheader()
            writer.writerows(data)
        print("✅ Fichier 'users_report.csv' créé avec succès.")
    except IOError:
        print("❌ Erreur : impossible d’écrire dans le fichier CSV.")
        return

    total_users = len(data)
    companies = sorted(set([user["Company"] for user in data if user["Company"]]))
    print(f"📊 Total users: {total_users} | Companies: {companies}")

if __name__ == "__main__":
    main()
