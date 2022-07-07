"""Main module"""
import os

from environs import Env
from pycoingecko import CoinGeckoAPI
from telebot import TeleBot

env = Env()
env.read_env()

bot = TeleBot(os.getenv("BOT_TOKEN"))
api = CoinGeckoAPI()


@bot.message_handler(content_types=["text"])
def crypto_price(message) -> None:
    """
    This handler will be called when user sends any text
    """
    crypto = message.text
    currency = "usd"
    response = api.get_price(ids=crypto, vs_currencies=currency)
    if not response:
        bot.send_message(message.chat.id, "Crypto not found, try another name")
        return
    bot.send_message(message.chat.id, f"{crypto}: {response[crypto][currency]} {currency}")


if __name__ == '__main__':
    bot.polling()
