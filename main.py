import asyncio
from os import getenv
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message



import requests

# 1 TOKEN = '***'

load_dotenv()
TOKEN = getenv('TOKEN')
dp = Dispatcher()


# Command handler
@dp.message(Command('start'))
async def command_start_handler(message: Message) -> None:
   await message.answer('Assalomu alaykum botga xush kelibsiz!')


@dp.message(Command('help'))
async def command_help_handler(message: Message) -> None:
   await message.answer('siz help chaqiruvini chaqirdiz!')




API_KEY = '***'

currency='USD'
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"
response = requests.get(url)
kurs = response.json()['conversion_rate']
# print(f"1 dollar kursi {kurs} so'mga teng")


@dp.message(Command('dollar'))
async def command_dollar_handler(message: Message) -> None:
   await message.answer(f'1 dollar kursi {kurs} somga teng')


api_key = '***'
city = 'Urgench'
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
data = requests.get(url).json()
k = data['main']['temp']

@dp.message(Command('weather'))
async def command_weather_handler(message: Message) -> None:
   await message.answer(f'Urganchdaki ob havo {k}C')



# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)
    await  dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())