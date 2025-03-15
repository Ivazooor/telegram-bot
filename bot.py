import os
import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Логирование
logging.basicConfig(level=logging.INFO)

# Обработчик сообщений
@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Бот запущен и готов к работе!")

@dp.message()
async def monitor_messages(message: Message):
    text = message.text.lower()
    
    # Ключевые слова для фиксации согласования
    keywords = ["прошу согласовать", "прошу принять решение", "прошу дать добро", "необходимо согласование"]
    
    if any(kw in text for kw in keywords):
        logging.info(f"Сообщение от {message.from_user.id} в чате {message.chat.id} содержит запрос согласования.")
        await message.reply("Запрос на согласование зафиксирован.")
    
    # Фиксация сроков
    if any(word in text for word in ["готово", "срок", "перенос", "подтверждаю"]):
        logging.info(f"Фиксируем срок или подтверждение в чате {message.chat.id}.")
        await message.reply("Срок или подтверждение зафиксированы.")

# Главная функция запуска бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
