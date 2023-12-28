import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.exceptions import TelegramNetworkError
from aiogram.filters import CommandStart
from dotenv import load_dotenv

from dialogs import setup_dialogs
from logs_hendler_telegram import TelegramBotHandler

from keyboards.reply import reply_markup

logger = logging.getLogger(__name__)


async def get_start(message: types.Message) -> None:
    await message.answer(f"Привет {message.from_user.first_name}!\n"
                         f"Я бот XELLA!!! "
                         f"Я могу показать список всех текущих акций, "
                         f"рассказать подробнее про каждую акцию.\n"
                         f"A также помогу сорентироватся какие из акций"
                         f" сумируются между собой, а какие нет.",
                         reply_markup=reply_markup)


async def connect_telegram():
    bot = Bot(token=telegram_token)
    dp = Dispatcher()
    setup_dialogs(dp)
    dp.message.register(get_start, CommandStart())
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
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    try:
        asyncio.run(connect_telegram())
    except TelegramNetworkError as con_err:
        logger.error(con_err)
