from fastapi import FastAPI, Request
from fastapi.middleware.gzip import GZipMiddleware
from pydantic import BaseModel
import requests as req

app = FastAPI()
app.add_middleware(GZipMiddleware, minimum_size=500)

class TelegramMessage(BaseModel):
    bot_token: str
    chat_id: str
    text: str

@app.get("/api/ping")
async def ping():    
    return {"message": "pong"}

@app.post("/api/webhook/telegram")
async def send_telegram(message: TelegramMessage):
    data = {
        "chat_id": message.chat_id,
        "text": message.text
    }

    response = req.post(
        f"https://api.telegram.org/bot{message.bot_token}/sendMessage", 
        data=data
    )
    
    if response.status_code == 200:
        return {"message": "ok"}
    else:
        return {
            "message": "error",
            "details": response.text
        }

@app.post("/api/webhook/telegram/raw")
async def send_telegram_raw(request: Request):
    body = await request.json()
    bot_token = body.get("bot_token")
    chat_id = body.get("chat_id")
    text = body.get("text")
    
    data = {
        "chat_id": chat_id,
        "text": text
    }

    response = req.post(
        f"https://api.telegram.org/bot{bot_token}/sendMessage", 
        data=data
    )
    
    if response.status_code == 200:
        return {"message": "ok"}
    else:
        return {
            "message": "error",
            "details": response.text
        }