# -*- coding: utf-8 -*-

from telebot.async_telebot import AsyncTeleBot
import asyncio
import requests

bot = AsyncTeleBot('6093920211:AAEV4C40nu-R7QZUYjxELoIiS5r-NXmYFwE')

print('Bot started...')


@bot.message_handler(commands=['start'])
async def start(message):
    text = f'Hello, <b>{message.from_user.first_name} {message.from_user.first_name}</b>!'
    # This Bot for you.
    # It All Comes Back 2 Crypto
    # """
    await bot.send_message(message.chat.id, text, parse_mode='html')
    text = """
    This is Bot for you!\nIt All Comes Back 2 Crypto"""
    await bot.send_message(message.chat.id, text, parse_mode='html')


@bot.message_handler(commands=['get_rates'])
async def get_rates(message):
    text = """ Currency Rates: 
        Binance - Tinkoff: 0
        Binance - Sber: 0
        """
    await bot.send_message(message.chat.id, text)


# if __name__ == 'main':
#     asyncio.run(bot.polling(none_stop=True, interval=0))

asyncio.run(bot.polling(none_stop=True, interval=0))
