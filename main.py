from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Microservice for managing clinical histories"}