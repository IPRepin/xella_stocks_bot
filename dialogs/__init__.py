from aiogram import Dispatcher
from aiogram_dialog import DialogRegistry

from . import change_stock


def setup_dialogs(dp: Dispatcher):
    registry = DialogRegistry(dp)
    for dialog in [
        *change_stock.change_stock_dialog()
    ]:
        registry.register(dialog)
