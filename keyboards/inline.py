from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from misc.db_comands import get_all_stocks

stocks_cd = CallbackData("show_stocks", "stocks_id")


def make_callback_data(stocks_id: int = 0):
    return stocks_cd.new(stocks_id=stocks_id)


async def choosing_promotion_keyboards():
    menu = InlineKeyboardMarkup()
    stocks = await get_all_stocks()
    for stock in stocks:
        button_text = f"{stock.name_stock}"
        callback_data = make_callback_data(stock.id)
        print(callback_data)

        menu.row(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )
    return menu
