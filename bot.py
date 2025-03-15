import os
import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InputFile
from aiogram import executor
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

# Обработчик сообщений
@dp.message_handler()
async def monitor_messages(message: types.Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    text = message.text.lower()

    # Фиксация ключевых слов
    keywords = ["прошу согласовать", "прошу принять решение", "прошу дать добро", "необходимо согласование"]
    if any(kw in text for kw in keywords):
        logging.info(f"Сообщение от {user_id} в чате {chat_id} содержит запрос согласования.")
        await message.reply("Запрос на согласование зафиксирован.")

    # Фиксация сроков
    if any(word in text for word in ["готово", "срок", "перенос", "подтверждаю"]):
        logging.info(f"Фиксируем срок или подтверждение в чате {chat_id}.")
        await message.reply("Срок или подтверждение зафиксированы.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
