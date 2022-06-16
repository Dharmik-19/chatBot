import telebot
from dotenv import load_dotenv 
import os 

load_dotenv() 


my_secret = os.getenv('TELEGRAM_API')
bot = telebot.TeleBot(my_secret) 


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello, I am a bot!")


@bot.message_handler()
def send_echo(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(non_stop=True)