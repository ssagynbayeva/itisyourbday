from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # for reply keyboard (sends message)

from time import sleep
from datetime import date
import numpy as np

today = date.today()
d = today.strftime("%d/%m")


bot = Bot(token='5747825338:AAErPHwrsyW26ffF31MHSORVW6Pmb9thk7k')
dp = Dispatcher(bot)

@dp.message_handler(commands=['today'])
async def bday(message: types.Message):
    fname = 'friends-bday.txt'
    name = np.loadtxt(fname,unpack=True, comments='#',dtype='U')
    dates = name[0]
    firstname = name[1]

    for i, date in enumerate(dates):
     if d == date:
            await bot.send_message(message.chat.id,'it is your birthday, {}'.format(firstname[i]))

# this is the last line
executor.start_polling(dp)