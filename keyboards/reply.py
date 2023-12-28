from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply_markup = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='°/•Сложить скидки'),
    ]
], resize_keyboard=True, input_field_placeholder="Для проверки скидок нажми кнопку⬇️")
