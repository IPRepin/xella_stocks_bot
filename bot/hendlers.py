from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart, Text

from keyboards.inline import choosing_promotion_keyboards, stocks_cd
from keyboards.reply import reply_markup
from misc.db_comands import get_stock
from misc.sort_stocks import sort_promotion


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


async def show_promotion(callback_query: types.CallbackQuery,
                         callback_data: dict
                         ) -> None:
    stock_id = int(callback_data.get("stocks_id"))
    stock = await get_stock(stock_id)
    stocks_lst = await sort_promotion(stock.category)
    stocks_lst = '\n'.join(stocks_lst)
    if stock.category == "A":
        text = (f"Акция '✅{stock.name_stock}' суммируется с одной из акций⬇️\n"
                f"{stocks_lst}")
    elif stock.category == "B":
        text = (f"Акция '✅{stock.name_stock}' суммируется с⬇️\n"
                f"{stocks_lst}")
    else:
        text = (f"Акция '⛔{stock.name_stock}'"
                f"не суммируется ни со одной акцией!")
    await callback_query.message.edit_text(text)


def register_hendlers(dp: Dispatcher):
    dp.register_message_handler(get_start, CommandStart())
    dp.register_message_handler(change_stocks, Text(equals="°/•Сложить скидки"))
    dp.register_callback_query_handler(show_promotion, stocks_cd.filter())
