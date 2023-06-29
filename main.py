from fastapi import FastAPI

# Instance of FastAPI()
app = FastAPI()

@app.get("/", description="This is our first route")
async def root():
    return {"message": "Hellow world"}