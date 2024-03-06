from fastapi import FastAPI

app = FastAPI()

# Endpoints

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/encrypt/{message}")
async def encrypt(message: str):
    return {"message": "Hello from the API!"}

@app.post("/decrypt/{message}")
async def decrypt(message: str):
    return {"message": "Decrypted message!"}

