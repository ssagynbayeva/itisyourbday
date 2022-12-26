from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # for reply keyboard (sends message)

from time import sleep
from datetime import date
import numpy as np
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging
import datetime

import schedule
import time

today = date.today()
d = today.strftime("%d/%m")

updater = Updater(token='5747825338:AAErPHwrsyW26ffF31MHSORVW6Pmb9thk7k', use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

bot = Bot(token='5747825338:AAErPHwrsyW26ffF31MHSORVW6Pmb9thk7k')
dp = Dispatcher(bot)

j = updater.job_queue

@dp.message_handler()
async def bday(message: types.Message):
    fname = 'friends-bday.txt'
    name = np.loadtxt(fname,unpack=True, comments='#',dtype='U')
    dates = name[0]
    firstname = name[1]

    for i, date in enumerate(dates):
     if d == date:
            await bot.send_message(message.chat.id,'it is your birthday, {}'.format(firstname[i]))


executor.start_polling(dp)