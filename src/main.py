from fastapi import FastAPI
from schemas.message import Message
from core.encryptor import encrypt, decrypt

app = FastAPI()

# Endpoints

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/encrypt")
async def encrypt_text(msg: Message):
    return {"message": encrypt(msg.shift, msg.content)}

@app.post("/decrypt")
async def decrypt_text(msg: Message):
    return {"message": decrypt(msg.shift, msg.content)}

