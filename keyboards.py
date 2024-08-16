from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


main = ReplyKeyboardMarkup(keyboard=[
   [KeyboardButton(text="Привет"),
   KeyboardButton(text="Пока")]
], resize_keyboard=True)

inline_links = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Новости", url="https://lenta.ru/")],
    [InlineKeyboardButton(text="Музыка", url="https://rutube.ru/video/34ffc5925f508b146bf69edc43fb94d6/")],
    [InlineKeyboardButton(text="Видео", url="https://rutube.ru/video/8d9c2167302bb22ccb7322b052c35062/")]
])

inline_more = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Показать больше", callback_data='more')]
])


options = [
    ['option1', 'Опция 1'],
    ['option2', 'Опция 2']
 ]
async def get_options():
    keyboard = InlineKeyboardBuilder()
    for key in options:
        keyboard.add(InlineKeyboardButton(text=key[1], callback_data=key[0]))
    return keyboard.as_markup()
