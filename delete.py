from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, \
    ReplyKeyboardRemove
from aiogram.types.message import ContentType
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "6181834925:AAE-stlojDhCEE1ndAqualhgfiLlYAGgPp4" # ваш токен

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

KB1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb1_1 = KeyboardButton("/help")
kb1_2 = KeyboardButton("/search")
KB1.add(kb1_1).insert(kb1_2)

KB3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb3_1 = KeyboardButton("/go")
kb3_2 = KeyboardButton("/search")
KB3.add(kb3_1).add(kb3_2)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="короткий текс от себя",
                           parse_mode="html",
                           reply_markup=KB1)
    await message.delete()


@dp.message_handler(commands=['country'])
async def send_welcome(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"любой текст ",
                           parse_mode="html")
    await bot.send_message(chat_id=message.from_user.id,
                           text=" любой текс ",
                           parse_mode="html",
                           reply_markup=KB3)
    await message.delete()
