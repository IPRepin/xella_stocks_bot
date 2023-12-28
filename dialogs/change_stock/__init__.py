from aiogram_dialog import Dialog

from dialogs.change_stock import windows


def change_stock_dialog():
    return [
        Dialog(
            windows.categoriues_stocks(),
            windows.stocks(),
            on_process_result=windows.on_process_result,
        ),
    ]
