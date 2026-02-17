import requests
import random

def obtenir_citation_trump():
    # L'URL de l'API pour une citation aléatoire
    url = "https://api.whatdoestrumpthink.com/api/v1/quotes/random"
    
    try:
        # Envoi de la requête GET
        response = requests.get(url)
        
        # Vérification que la requête a réussi (code 200)
        response.raise_for_status()
        
        # Extraction des données JSON
        data = response.json()
        
        # La citation se trouve dans la clé 'message'
        return data['message']
    
    except requests.exceptions.RequestException as e:
        return f"Erreur lors de la connexion à l'API : {e}"

if __name__ == "__main__":
    print("--- Citation Aléatoire de Donald Trump ---")
    citation = obtenir_citation_trump()
    print(f"\n\"{citation}\"\n")
    print("------------------------------------------")