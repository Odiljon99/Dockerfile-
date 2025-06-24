import os
import logging
from flask import Flask, request
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Update
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")

app = Flask(__name__)
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@app.post(f"/webhook/{WEBHOOK_SECRET}")
async def handle_webhook():
    update = Update.model_validate(request.json)
    await dp.feed_update(bot, update)
    return {"status": "ok"}

@app.route("/", methods=["GET"])
def home():
    return "Bot is running!"

async def main():
    logging.basicConfig(level=logging.INFO)
    # Здесь ты можешь добавить хендлеры, команды и т.п.

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))