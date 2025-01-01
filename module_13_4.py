from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio


api = "" # Переменная в которой хранится ключ от телеграм-бота
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

class UserState(StatesGroup):
    adress = State()

@dp.message_handler(text = 'Заказать')
async def buy(message):
    await message.answer('Отправь нам свой адрес')
    await UserState.adress.set()

@dp.message_handler(state = UserState.adress)
async def fsm_handler(message, state):
    await state.update_data(first = message.text)
    data = await state.get_data()
    await message.answer(f'Доставка будет отправлена на {data["first"]}')
    await state.finish()




class UserState(StatesGroup):
    age =State()
    growth = State()
    weight = State()

@dp.message_handler(text = ['Расчёт калорий'])
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
    await message.answer(f'Ваша суточная норма калорий {10 * int(date["thrist"]) + 6.25 * int(date["second"]) - 5 * int(date["first"]) + 5}')
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
