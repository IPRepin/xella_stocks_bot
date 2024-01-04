from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart, Text

from keyboards.inline import choosing_promotion_keyboards
from keyboards.reply import reply_markup


async def get_start(message: types.Message) -> None:
    await message.answer(f"Привет {message.from_user.first_name}!\n"
                         f"Я бот XELLA!!! "
                         f"Я могу показать список всех текущих акций, "
                         f"рассказать подробнее про каждую акцию.\n"
                         f"A также помогу сорентироватся какие из акций"
                         f" сумируются между собой, а какие нет.",
                         reply_markup=reply_markup)


async def change_stocks(message: types.Message) -> None:
    menu = await choosing_promotion_keyboards()
    await message.answer("Выбери нужную акцию⬇️", reply_markup=menu)


def register_hendlers(dp: Dispatcher):
    dp.register_message_handler(get_start, CommandStart())
    dp.register_message_handler(change_stocks, Text(equals="°/•Сложить скидки"))