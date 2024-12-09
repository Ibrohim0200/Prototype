from aiogram import types, Dispatcher, Bot
from aiogram.filters import Command
import asyncio
from random import randint

TOKEN ="7789052663:AAF4aWbPspPGy1abAnqkj59Icyw_w-6Dooc"
bot = Bot(token=TOKEN)
dp = Dispatcher()

user_data ={}

@dp.message()
async def handle_message(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_data or message.text == '/start':
        await start(message)
    elif 'phone' not in user_data[user_id]:
        await send_code(message)
    elif 'status' not in user_data[user_id]:
        await chek_code(message)
    elif 'location' not in user_data[user_id]:
        await save_address(message)
    elif 'kategoriyalar' in user_data[user_id]['keyboard']:
        await show_menu(message)
    elif 'tovarlar' in user_data[user_id]['keyboard']:
        await show_item(message)
    elif 'tanlangan_tovar' in user_data[user_id]['keyboard']:
        await select_item(message)

@dp.message(Command("start"))
async def start(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id] = {}
    button = [
        [types.KeyboardButton(text="Share contact", request_contact=True)],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, one_time_keyboard=True, resize_keyboard=True)
    await message.answer(f"Assalomu alaykum! Les Ailes yetkazib berish"
                         f"xizmatiga xush kelibsiz!\n"
                         f"Iltimos telefon raqamingizni kiriting:", reply_markup=keyboard)
