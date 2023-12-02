import requests
import time

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, \
    ReplyKeyboardRemove
from aiogram.types.message import ContentType
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "6803275134:AAE4Mru7BwHbZDbGAG5u9d2JdpDbVbBZQDI"  # ваш токен

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

KB1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb1_1 = KeyboardButton("/help")
kb1_2 = KeyboardButton("/🌠")
kb1_3 = KeyboardButton("/🌤")
kb1_4 = KeyboardButton("👨🏻‍💻")
kb1_5 = KeyboardButton("/end")
KB1.add(kb1_1)
KB1.add(kb1_3).insert(kb1_2)

KB3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb3_1 = KeyboardButton("/go")
kb3_2 = KeyboardButton("/search")
KB3.add(kb3_1).add(kb3_2)

user_text = None


def gen_photo_url(word: str) -> str:
    return "https://yandex.ru/images/search?text=" + word

def gen_weather_outer(city):

def gen_video_url(city):
    return "https://ya.ru/video/preview/739561961099189934" + city + "/details"

def gen_end_url(city) -> str:
    return "https://yandex.ru/images/search?text=" + city + "/details"

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="короткий текст от себя",
                           parse_mode="html",
                           reply_markup=KB1)
    await message.delete()

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Мой чат бот умеет прогназировать погоду в разных точках мира "
                                "и отправлять фотографии, которые вы хотите например: кота или же машину",
                           parse_mode="html",
                           reply_markup=KB1)


@dp.message_handler(commands=['end'])
async def send_end(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Спасибо, за то что воспользовались моим Телеграм Чат Ботом."
                                "Надеюсь вы будете пользоваться с ним ещё. ",
                           parse_mode="html",
                           reply_markup=KB1)
    await message.delete()

@dp.message_handler()
async def echo(message: types.Message):
    global user_text
    if message.text[0] != '/':
        user_text = message.text
    elif message.text == '/🌠':
        if user_text is None:
            await bot.send_message(chat_id=message.from_user.id,
                                   text="вы еще ничего не ввели")
        else:
            await bot.send_photo(chat_id=message.from_user.id,
                                 photo=gen_photo_url(user_text))
            await message.delete()
            user_text = None
    elif message.text == '/🌤':
        if user_text is None:
            await bot.send_message(chat_id=message.from_user.id,
                                   text="вы еще ничего не ввели")
        else:
            await bot.send_message(chat_id=message.from_user.id,
                                   text=gen_weather_outer(user_text))
            await message.delete()
            user_text = None
    elif message.text == '/👨🏻‍💻':
        if user_text is None:
            await bot.send_message(chat_id=message.from_user.id,
                                   text="вы еще ничего не ввели")
        else:
            await bot.send_message(chat_id=message.from_user.id,
                                   text=gen_video_url(user_text))
            await message.delete()
            user_text = None

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)

