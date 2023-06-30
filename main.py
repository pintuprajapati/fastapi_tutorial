from enum import Enum
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

# Instance of FastAPI()
app = FastAPI()

@app.get("/", description="This is our first route")
async def root():
    return {"message": "Hellow world"}

##### Path Parameters #####

# create endpoint in order because FastAPI executes endpoints orderwise
# specify the static endpoint first and then dynamic or the other way around (as per requirement)
@app.get("/users/me", description="this is second route")
def get_current_user():
    return {"message": "This is the current user"}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id}

@app.get("/calculate/{number}")
async def calculate(number:int):
    result = 5 + number
    return {
        "message": "this is calculation",
        "data": result
    }

################### Create a Model and Endpoint using that model ###################
class FoodEnum(str, Enum):
    """ Model """
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"

# endpoint: get_food()
@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    # food_name is instance of FoodEnum

    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name, "message": "You eat vegetables, so you are healthy"}
    
    if food_name.value == "fruits":
        return {"food_name": food_name, "message": "You eat fruits, so you are sweet and healthy"}
    
    return {"food_name": food_name, "message": "I like chocolates"}


##### Query Parameters #####
# (http://127.0.0.1:8000/items/1?q=hi&short=True)
@app.get("/items/{item_id}")
async def get_item(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({
            "description": "The brown fox jumps over the lazy dog"
        })
    return item

##### Request Body #####
# pydantic model
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# POST endpoint
@app.post("/items")
async def create_item(item: Item):
    item_dict = item.dict() # it will be converted to dic()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

# PUT endpoint
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result