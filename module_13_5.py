
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup #
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton #
import asyncio


api = ""
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

kd = ReplyKeyboardMarkup()
button = KeyboardButton(text = 'Рассчитать')
button_2 = KeyboardButton(text = 'Информация')
button_10 = KeyboardButton(text = 'Информация 9')
kd.add(button)
kd.add(button_2)
kd.add(button_10)
resize_keyboard=True

@dp.message_handler(commands = ['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup = kd)

@dp.message_handler(text = 'Информация')
async def info(message):
    await message.answer('Я умею расчитывать среднесуточное количество калорий')


class UserState(StatesGroup):
    age =State()
    growth = State()
    weight = State()

@dp.message_handler(text = ['Рассчитать'])
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(first = message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(second=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(thrist=message.text)
    date = await state.get_data()
    await message.answer(f'Ваша суточная норма калорий'
                         f' {10 * int(date["thrist"]) + 6.25 * int(date["second"]) - 5 * int(date["first"]) + 5}')
    await state.finish()

@dp.message_handler(text = 'Информация 9')
async def info(message):
    await message.answer('Что-то я должен сделать, но что не знаю')



@dp.message_handler()
async def all_message(message):
    await message.answer(f'Введите команду /start, чтобы начать общение')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
