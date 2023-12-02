import time
import requests

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, \
    ReplyKeyboardRemove
from aiogram.types.message import ContentType
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "6181834925:AAE-stlojDhCEE1ndAqualhgfiLlYAGgPp4"  # ваш токен

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

KB1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb1_1 = KeyboardButton("/help")
kb1_2 = KeyboardButton("/🌠")
kb1_3 = KeyboardButton("/🌤")
kb1_4 = KeyboardButton("/✨")
KB1.add(kb1_1).insert(kb1_4)
KB1.add(kb1_3).insert(kb1_2)

KB3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb3_1 = KeyboardButton("/go")
kb3_2 = KeyboardButton("/search")
KB3.add(kb3_1).add(kb3_2)

user_text = None


def gen_photo_url(word: str) -> str:
    return "https://yandex.ru/images/search?text=" + word


def gen_weather_outer(city):
    return "https://yandex.ru/weather/ru-RU/" + city + "/details"


def gen_video_url(word):
    return "https://www.youtube.com/results?search_query=" + word


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="короткий текс от себя",
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
    elif message.text == '/✨':
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
