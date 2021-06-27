import logging
import settings
import telebot
import webbrowser
import requests
import time
import json
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from telebot import types


ip_adrr = ''
ip_adr = ''
URL = ''
URL1 = ''
Nomer_kvartiri = ''
bot = telebot.TeleBot(settings.TOKEN)


@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет")
    elif message.text == '/rebot':
        bot.send_message(message.from_user.id, "Ввиди ip-адрес!")
        bot.register_next_step_handler(message, reboot_beward)
    elif message.text == '/zvonok':
        bot.send_message(message.from_user.id, "Ввиди ip-адрес!")
        bot.register_next_step_handler(message, zvonok_beward)


def reboot_beward(message):
    global ip_adrr
    global URL
    ip_adrr = message.text
    URL = "http://" + ip_adrr + "/cgi-bin/restart_cgi?&user=admin&pwd=admin"
    webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))
    webbrowser.open_new(URL)


def zvonok_beward(message):
    global ip_adr
    
    ip_adr = message.text
    bot.send_message(message.from_user.id, "Ввиди номер квартиры")
    bot.register_next_step_handler(message, zvonok1_beward) 
    
    URL_GET = "http://" + ip_adr + "/cgi-bin/apartment_cgi?action=get&Number=3"
    
    print(URL_GET)
def zvonok1_beward(message):
    global URL1
    global Nomer_kvartiri
    Nomer_kvartiri = message.text
    
    URL1 = "http://" + ip_adr + "/cgi-bin/sip_cgi?action=call&Uri=" +Nomer_kvartiri + "&user=admin&pwd=admin"
    webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))
    webbrowser.open_new(URL1)
    print(URL1)

bot.polling()
