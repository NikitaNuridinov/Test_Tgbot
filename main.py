from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, \
    ReplyKeyboardRemove
from aiogram.types.message import ContentType
from aiogram import Bot, Dispatcher, types, executor


API_TOKEN = "6181834925:AAE-stlojDhCEE1ndAqualhgfiLlYAGgPp4"


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

KB1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb1_1 = KeyboardButton("/help")
kb1_2 = KeyboardButton("/search")
KB1.add(kb1_1).insert(kb1_2)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="""
<em><b>Добро пожаловать на сервис по подбору автомобилей!</b>
Поиск можно производить по странам производителей,
либо искать машины определенного бренда</em>
В случае если вы решите начать поиск сначала,
вызовите команду /search
                            """,
                           parse_mode="html",
                           reply_markup=KB1)
    await message.delete()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
