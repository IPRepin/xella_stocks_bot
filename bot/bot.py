import asyncio
import logging
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'admin_panel.admin_panel.settings')
os.environ.update({"DJANGO_ALLOW_ASYNC_UNSAFE": "true"})
django.setup()

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv

from hendlers import register_hendlers
from logs_hendler_telegram import TelegramBotHandler

logger = logging.getLogger(__name__)


async def connect_telegram():
    bot = Bot(token=telegram_token)
    dp = Dispatcher(bot, loop=bot.loop, storage=MemoryStorage())
    register_hendlers(dp)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.close()


if __name__ == '__main__':
    load_dotenv()
    telegram_log_handler = TelegramBotHandler()
    logging.basicConfig(handlers=[telegram_log_handler],
                        level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    project_id = os.getenv("DIALOGFLOW_ID")
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    try:
        asyncio.run(connect_telegram())
    except KeyboardInterrupt:
        logger.info('Bot interrupted')
