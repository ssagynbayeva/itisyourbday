from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # for reply keyboard (sends message)

from time import sleep


bot = Bot(token='5747825338:AAErPHwrsyW26ffF31MHSORVW6Pmb9thk7k')
dp = Dispatcher(bot)

answers = []  # store the answers they have given


### add stuff here


# this is the last line
executor.start_polling(dp)