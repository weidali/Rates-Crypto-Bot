# !/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio
import os
import requests
import telebot
from dotenv import load_dotenv
from telebot import types
from telebot.async_telebot import AsyncTeleBot

load_dotenv()
bot = AsyncTeleBot(os.getenv("TELEGRAM_BOT_KEY"))
print('Bot started...')


async def main():
    await bot.delete_my_commands(scope=None, language_code=None)

    await bot.set_my_commands(
        commands=[
            telebot.types.BotCommand("get_rates", "Binance rates"),
            telebot.types.BotCommand("help", "Commands List")
        ],
        # scope=telebot.types.BotCommandScopeChat(12345678)  # use for personal command menu for users
        # scope=telebot.types.BotCommandScopeAllPrivateChats()  # use for all private chats
    )

    cmd = await bot.get_my_commands(scope=None, language_code=None)
    print([c.to_json() for c in cmd])


if __name__ == '__main__':
    asyncio.run(main())

# @bot.message_handler(commands=['start'])
# async def start(message):
#     markup = types.InlineKeyboardMarkup
#
#     text = f"""Hello, <b>{message.from_user.first_name} {message.from_user.first_name}</b>,\nThis Bot for you!\nIt All Comes Back 2 Crypto"""
#     await bot.send_message(message.chat.id, text, parse_mode='html')
#
#
# @bot.message_handler(commands=['help'])
# async def help(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#     get_rates = types.KeyboardButton('Rates')
#     start = types.KeyboardButton('Start')
#     markup.add(get_rates, start)
#     await bot.send_message(message.chat.id, 'text', reply_markup=markup)
#
#
# @bot.message_handler(commands=['get_rates'])
# async def get_rates(message):
#     binance_tinkoff_rate = get_binance_rates()
#     text = f""" Currency Rates:
#         Binance - Tinkoff: {binance_tinkoff_rate}
#         Binance - Sber: 0
#         """
#     await bot.send_message(message.chat.id, text)
#
#
# def get_binance_rates():
#     url = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'
#     url = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'
#     headers = {
#         'Accept': '*/*',
#         'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0',
#     }
#     params = {
#         "fiat": "RUB",
#         "page": 1,
#         "rows": 10,
#         "transAmount": 100,
#         "tradeType": "BUY",
#         "asset": "USDT",
#         "countries": [],
#         "proMerchantAds": False,
#         "publisherType": None,
#         "payTypes": ["TinkoffNew"]
#     }
#
#     response = requests.post(url, headers=headers, json=params).json()
#     print(response)
#     return response['data'][0]['adv']['price']
#
#
# # if __name__ == 'main':
# #     asyncio.run(bot.polling(none_stop=True, interval=0))
#
# asyncio.run(bot.polling(none_stop=True, interval=0))
