import requests


def requete_exemple():
    requete = requests.get(
        "https://world.openfoodfacts.org/api/v0/product/3256540001305.json")
    print("requete_exemple(): " + str(requete.status_code))    
    return requete.json()
