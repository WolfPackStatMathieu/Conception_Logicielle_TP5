from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


from app.model import get_ingredients, is_vegan, requete_exemple

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
