from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types.message import ContentType
from aiogram import Bot, Dispatcher, executor, types

# from carInfo import SearchError as SE
from carInfo import Car as C
from carInfo import CarFilter as CF


API_TOKEN = "6181834925:AAE-stlojDhCEE1ndAqualhgfiLlYAGgPp4"


class CarID():
    def __init__(self):
        self.id = 0
    def forward(self):
        self.id = self.id + 1
    def back(self):
        self.id = self.id - 1


def href_brand(c):
    lt = list()
    for car in c:
        lt.append(
            f'<a href = "https://auto.drom.ru/{car.replace(" ", "_")}">{car.upper()}</a>')
    return lt


def href_model(brand, model):
    return f'<a href = "https://auto.drom.ru/{brand.replace(" ", "_").lower()}/{model.replace(" ", "_").lower()}"><em>ссылка на дром</em></a>'


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

KB1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb1_1 = KeyboardButton("/help")
kb1_2 = KeyboardButton("/search")
KB1.add(kb1_1).insert(kb1_2)


KB2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb2_1 = KeyboardButton("/country")
kb2_2 = KeyboardButton("/brand")
KB2.add(kb2_1).insert(kb2_2)


KB3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb3_1 = KeyboardButton("/go")
kb3_2 = KeyboardButton("/search")
KB3.add(kb3_1).add(kb3_2)


KB4 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb4_1 = KeyboardButton("/yes")
kb4_2 = KeyboardButton("/search")
KB4.add(kb4_1).add(kb4_2)


KB5 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb5_1 = KeyboardButton("⬅️")
kb5_2 = KeyboardButton("/search")
kb5_3 = KeyboardButton("➡️")
KB5.add(kb5_1).insert(kb5_2).insert(kb5_3)


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


@dp.message_handler(commands=["help"])
async def help_message(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="""
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>запуск</em>
<b>/search</b> - <em>начать поиск машины</em>
<b>/country</b> - <em>выбор страны производителя </em>
<b>/brand</b> - <em>выбор определенной марки </em>
                           """,
                           parse_mode="html",
                           reply_markup=KB1)
    await message.delete()


@dp.message_handler(commands=['search'])
async def send_search(message: types.Message):
    global car_id
    car_id = CarID()
    global cars
    cars = CF()
    await bot.send_message(chat_id=message.from_user.id,
                           text="""
<b>/country</b> - <em>выбор страны производителя </em>
<b>/brand</b> - <em>выбор определенной марки </em>
""",
                           parse_mode="html",
                           reply_markup=KB2)
    await message.delete()


# ----------------> Страны

@dp.message_handler(commands=['country'])
async def send_welcome(message: types.Message):
    lt = cars.getCountry()
    lt = str(lt).replace(",", "\n").replace(
        "{", "").replace("}", "").replace("'", "").title()
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"""
<b>страны:</b>
{lt}
                            """,
                           parse_mode="html")
    await bot.send_message(chat_id=message.from_user.id,
                           text="""
Введите нужную вам страну и напишите её следущим сообщением!
<em><b>!Пишите без ошибок!</b></em>
<em><b>! отправить /go !</b></em>
                           """,
                           parse_mode="html",
                           reply_markup=KB3)
    await message.delete()


# ----------------> Бренды

@dp.message_handler(commands=['brand'])
async def send_welcome(message: types.Message):
    lt = cars.getBrand()
    lt = sorted(list(lt))
    lt = str(lt).replace(",", "\n").replace(
        "[", "").replace("]", "").replace("'", "").title()
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"""
<b>Бренды авто:</b>
{lt}
                            """,
                           parse_mode="html")
    await bot.send_message(chat_id=message.from_user.id,
                           text="""
Найдите нужный вам бренд и отправьте его следующим сообщением!
<em><b>!Пишите без ошибок!</b></em>
<em><b>! отправить /yes !</b></em>
                           """,
                           parse_mode="html",
                           reply_markup=KB4)
    await message.delete()


# ----------------> обработчик

@dp.message_handler()
async def echo(message: types.Message):
    global tx
    if message.text not in ['/go', '/yes', '⬅️', '➡️']:
        tx = message.text

    if message.text == '/go':
        cars.countryfilter(tx)
        lt = cars.getBrand()
        lt = href_brand(lt)
        lt = str(lt).replace(",", "\n").replace(
            "[", "").replace("]", "").replace("'", "")
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"""
<b>список машин:</b>
{lt}
                                   """,
                               parse_mode="html",
                               reply_markup=KB1)
        await message.delete()

    elif message.text == '/yes':
        cars.brandfilter(tx)
        global car_lt
        car_lt = cars.carlist
        car = C(car_lt[car_id.id])
        car_href = href_model(car.brand(), car.model())
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=car.image())
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"""
<b>марка: </b>{car.brand()}
<b>модель: </b>{car.model()}
<b>страна производитель: </b>{car.country()}
<b>год выпуска первой модели: </b>{car.release()}
<b>год самой актуальной версии: </b>{car.lastyear()}
{car_href}
                               """,
                               parse_mode="html",
                               reply_markup=KB5)
        await message.delete()

    elif message.text == '⬅️':
        if abs(car_id.id) > len(car_lt):
            car_id.id = 0-1
        else:
            car_id.back()
        car = C(car_lt[car_id.id])
        car_href = href_model(car.brand(), car.model())
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=car.image())
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"""
<b>марка: </b>{car.brand()}
<b>модель: </b>{car.model()}
<b>страна производитель: </b>{car.country()}
<b>год выпуска первой модели: </b>{car.release()}
<b>год самой актуальной версии: </b>{car.lastyear()}
{car_href}
                               """,
                               parse_mode="html",
                               reply_markup=KB5)
        await message.delete()
        
    elif message.text == '➡️':
        if abs(car_id.id) >= len(car_lt)-1:
            car_id.id = 0
        else:
            car_id.forward()
        car = C(car_lt[car_id.id])
        car_href = href_model(car.brand(), car.model())
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=car.image())
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"""
<b>марка: </b>{car.brand()}
<b>модель: </b>{car.model()}
<b>страна производитель: </b>{car.country()}
<b>год выпуска первой модели: </b>{car.release()}
<b>год самой актуальной версии: </b>{car.lastyear()}
{car_href}
                               """,
                               parse_mode="html",
                               reply_markup=KB5)
        await message.delete()
        await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)


# """
# Покупка
# """

# PAY_TOKEN = "**********:TEST:********************"

# PRICE = types.LabeledPrice(label="Покупка машины", amount=5*100)

# @dp.message_handler(commands=['buy'])
# async def buy(message: types.Message):
#     if PAY_TOKEN.split(':')[1] == 'TEST':
#         await bot.send_message(message.chat.id, "Тестовый платеж!!!")
#     await bot.send_invoice(message.chat.id,
#                            title="Покупка автомобиля",
#                            description="Ваш автомабиль готов к покупке",
#                            provider_token=PAY_TOKEN,
#                            currency="rub",
#                            photo_url="https://i.infocar.ua/i/2/6290/119582/1920x.jpg",
#                            photo_width=416,
#                            photo_height=234,
#                            photo_size=416,
#                            is_flexible=False,
#                            prices=[PRICE],
#                            start_parameter="one-car-sell",
#                            payload="test-invoice-payload")


# @dp.pre_checkout_query_handler(lambda query: True)
# async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
#     await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


# @dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
# async def successful_payment(message: types.Message):
#     print("SUCCESSFUL PAYMENT:")
#     payment_info = message.successful_payment.to_python()
#     for k, v in payment_info.items():
#         print(f"{k} = {v}")

#     await bot.send_message(message.chat.id,
#                            f"Платеж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошел успешно!!!")
