from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # for reply keyboard (sends message)

from time import sleep
from datetime import date
import numpy as np

today = date.today()
d = today.strftime("%d/%m")

fname = 'friends-bday.txt'
name = np.loadtxt(fname,unpack=True, comments='#',dtype='U')
dates = name[0]
firstname = name[1]

for i, date in enumerate(dates):
    if d == date:
        print('it is your birthday, {}'.format(firstname[i]))