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

async def send_code(message: types.Message):
    user_id = message.from_user.id
    if message.contact is not None:
        phone = message.contact.phone_number
    else:
        phone = message.text
    flag = False
    if phone[0:4] == '+998' or phone[0:3] =='998':
        if len(phone) == 12:
            phone = phone
        elif len(phone) == 13:
            phone = phone[1:]
        for s in phone:
            if s in '0123456789':
                flag = True
            else:
                flag = False
                break
    if flag == True:
        user_data[user_id]['phone'] = phone
        verification_code = randint(1000, 9999)
        user_data[user_id]["verification_code"] = verification_code
        await message.answer(f"Iltimos tasdiqlash raqamini kiriting: {verification_code}")
    else:
        await message.answer(f"Togri raqam kiriting:")
