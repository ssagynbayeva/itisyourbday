from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # for reply keyboard (sends message)

from time import sleep


bot = Bot(token='5747825338:AAErPHwrsyW26ffF31MHSORVW6Pmb9thk7k')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
	await message.reply("Hi! I am it is your birthday bot!")

@dp.message_handler()
async def echo(message: types.Message):
	await message.answer(message.text)

# this is the last line
executor.start_polling(dp)