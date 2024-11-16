from aiogram import Bot, Dispatcher, executor, types            #Импортируем сущность бота, диспетчера, «executor», типы
from aiogram.contrib.fsm_storage.memory import MemoryStorage    #блока работы с памятью
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = "7899637913:AAE-qnqGqAZvGEeSSHLoj9cfow2EmYjVmSY"
bot = Bot(token = api)                                  #Дальше понадобится api ключ, который мы получили в «BotFather». Так же переменная бота, она будет хранить объект бота, «token» будет равен вписанному ключу
dp = Dispatcher(bot, storage = MemoryStorage())          #Понадобится «Dispatcher», который будет объектом «Dispatcher», у него будет наш бот в качестве аргументов. В качестве «Storage» будет «MemoryStorage»

class UserState(StatesGroup):
    address = State()

@dp.message_handler(text = 'Заказать')
async def buy(message):
    await message.answer("Отправь нам свой адрес, пожалуйста")  #ожидание получения сообщения от пользователя
    await UserState.address.set()                               #для установки состояния и записи адреса

@dp.message_handler(state=UserState.address)                    #обработано не обычным хендлером, а хендлером состояния «@dp.message_handler()».
async def sm_handler(message, state):                        #когда хендлер сработает, вы получите два объекта: «message» и «state», который представляет текущее состояние пользователя
    await state.update_data(first=message.text)                             #позволяет обновить данные, связанные с текущим состоянием пользователя
    data = await state.get_data()                                    #метод позволяет вернуть все данные, связанные с текущим состоянием пользователя
    await message.answer(f"Доставка будет отправлена на {data['first']}")    #вывести адрес, сохраненный под ключом «first»
    await state.finish()                                                   #машина состояний завершила работу, ее необходимо закрыть с помощью метода
    




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)          #Запускаем «executor», у которого есть функция «start_polling». Объясняем, через кого ему запускаться
