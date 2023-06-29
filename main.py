from enum import Enum
from fastapi import FastAPI

# Instance of FastAPI()
app = FastAPI()

@app.get("/", description="This is our first route")
async def root():
    return {"message": "Hellow world"}

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
