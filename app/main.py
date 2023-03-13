from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None
    

@app.get("/")
def read_root():
    retour_exemple = requete_exemple()
    ingredients = get_ingredients(retour_exemple)
    est_vegan = is_vegan(ingredients)
    return {"Hello": "World",
            # "ingredients": ingredients,
            "veganitude": est_vegan
            }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


def requete_exemple():
    requete = requests.get(
        "https://world.openfoodfacts.org/api/v0/product/3256540001305.json")
    print("requete_exemple(): " + str(requete.status_code))    
    return requete.json()


def get_ingredients(request_json):
    print(request_json["product"]["ingredients"])
    return request_json["product"]["ingredients"]


def is_vegan(ingredients):
    is_vegan = True
    for ingredient in ingredients:
        if "vegan" in ingredient:
            if ingredient["vegan"] != "yes":
                is_vegan = False
    return is_vegan
