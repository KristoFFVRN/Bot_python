import logging
import settings
import telebot
import webbrowser
import requests
import time
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from telebot import types


ip_adrr = ''
URL = ''
bot = telebot.TeleBot(settings.TOKEN)


@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет")
    elif message.text == '/rebot':
        bot.send_message(message.from_user.id, "Ввиди ip-адрес!")
        bot.register_next_step_handler(message, ip_beward)


def ip_beward(message):
    global ip_adrr
    global URL
    ip_adrr = message.text
    URL = "http://" + ip_adrr + "/cgi-bin/restart_cgi?&user=admin&pwd=admin"
    webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser(
        'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))
    webbrowser.open_new(URL)
    print(URL)


bot.polling()
