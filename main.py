from config import TOKEN

import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
import aiohttp

import keyboards as kb

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
   await message.answer("Привет", reply_markup=kb.main)

@dp.message(F.text == 'Привет')
async def button1(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}')

@dp.message(F.text == 'Пока')
async def button1(message: Message):
    await message.answer(f'До свидания, {message.from_user.first_name}')

@dp.message(Command('links'))
async def links(message: Message):
    await message.answer(f'Вот ссылки', reply_markup=kb.inline_links)

@dp.message(Command('dynamic'))
async def links(message: Message):
    await message.answer(f'Нажми на кнопку', reply_markup=kb.inline_more)

@dp.callback_query(F.data == 'more')
async def news(callback: CallbackQuery):
   await callback.answer("Опции" )  #, show_alert=True)
   await callback.message.answer('Есть варианты:', reply_markup=await kb.get_options())

@dp.callback_query(F.data.in_({'option1', 'option2'}))
async def callback_option1(callback: CallbackQuery):
    await callback.answer("Опция")  # , show_alert=True)
    await callback.message.answer(get_option(callback.data))

def get_option(data):
    for option in kb.options:
        if option[0] == data:
            return option[1]

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())