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
ip_addr = ''
URL = ''
URL1 = ''
URL_GET = ''
Nomer_kvartiri = ''

nomer = 0
bot = telebot.TeleBot(settings.TOKEN)


@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет!")
    elif message.text == '/rebot':
        bot.send_message(message.from_user.id, "Введите ip-адрес!")
        bot.register_next_step_handler(message, reboot_beward)
    elif message.text == '/zvonok':
        bot.send_message(message.from_user.id, "Введите ip-адрес!")
        bot.register_next_step_handler(message, zvonok_beward)
    elif message.text == '/backup':
        bot.send_message(message.from_user.id, "Введите ip-адрес!")
        bot.register_next_step_handler(message, backup_beward)
    elif message.text == '/version':
        bot.send_message(message.from_user.id, "Введите ip-адрес!")
        bot.register_next_step_handler(message, version_beward) 
    elif message.text == '/blockcms':
        bot.send_message(message.from_user.id, "Введите ip-адрес!")
        bot.register_next_step_handler(message, BlockCMS_beward)       
def reboot_beward(message):
    global ip_adrr
    global URL
    ip_adrr = message.text
    URL = "http://" + ip_adrr + "/cgi-bin/restart_cgi?&user=admin&pwd=admin"
    bot.send_message(message.from_user.id, URL)

def zvonok_beward(message):
    global ip_adr
    ip_adr = message.text
    bot.send_message(message.from_user.id, "Введите номер дозвона!")
    bot.register_next_step_handler(message, zvonok1_beward)

def zvonok2_beward(message):
    global nomer
    if message.text != 0:
        nomer= message.text
        URL_GET = "http://" + ip_adr + "/cgi-bin/apartment_cgi?action=get&Number="+nomer+ "&user=admin&pwd=admin"
        bot.send_message(message.from_user.id, "Ввидите номер дозвона!")
    bot.register_next_step_handler(message, zvonok1_beward) 
    
def zvonok1_beward(message):
    global URL1
    global Nomer_kvartiri
    Nomer_kvartiri = message.text
    URL1 = "http://" + ip_adr + "/cgi-bin/sip_cgi?action=call&Uri=" +Nomer_kvartiri + "&user=admin&pwd=admin"
    bot.send_message(message.from_user.id, URL1)

    
def backup_beward(message):
    global ip_addr
    ip_addr = message.text
    global URL
    bot.send_message(message.from_user.id,'Сохранение бекапаов панели:')
    bot.send_message(message.from_user.id,'Cохранение №1: BAK-файл')  
    URL = "http://" + ip_addr + "/cgi-bin/config_cgi?action=backup&user=admin&pwd=admin"
    bot.send_message(message.from_user.id, URL)
    bot.send_message(message.from_user.id,'Cохранение №2: backup-ключей')  
    URL = "http://" + ip_addr + "/cgi-bin/rfid_cgi?action=export&user=admin&pwd=admin"
    bot.send_message(message.from_user.id, URL)
    bot.send_message(message.from_user.id,'Cохранение №3: backup-ККМ')  
    URL = "http://" + ip_addr + "/cgi-bin/intercomdu_cgi?action=export&user=admin&pwd=admin"
    bot.send_message(message.from_user.id, URL)

def BlockCMS_beward(message):
    global Nomer_kvartiri
    global ip_addr
    ip_addr = message.text
    bot.send_message(message.from_user.id, "Введите номер квартиры!")
    bot.register_next_step_handler(message, BlockCMS_1_beward)
    #bot.send_message(message.from_user.id, "Что надо сделать?")
    #bot.register_next_step_handler(message, BlockCMS_1_beward)
    #if message.text == "Заблокировать":
     #   URL1 = "http://" + ip_adr + "/cgi-bin/apartment_cgi?action=set&Number=" +Nomer_kvartiri + "&BlockCMS=off&user=admin&pwd=admin"
    #else:
        #URL1 = "http://" + ip_adr + "/cgi-bin/apartment_cgi?action=set&Number=" +Nomer_kvartiri + "&BlockCMS=on&user=admin&pwd=admin"   
    #bot.send_message(message.from_user.id, URL1)


def BlockCMS_1_beward(message):
    global URL1
    global Nomer_kvartiri
    global ip_addr
    Nomer_kvartiri = message.text
    bot.send_message(message.from_user.id, "Заблокировать:")
    URL1 = "http://" + ip_addr + "/cgi-bin/apartment_cgi?action=set&Number=" +Nomer_kvartiri + "&BlockCMS=off&user=admin&pwd=admin"
    bot.send_message(message.from_user.id, URL1)
    bot.send_message(message.from_user.id, "Разблокировать:")
    URL1 = "http://" + ip_addr + "/cgi-bin/apartment_cgi?action=set&Number=" +Nomer_kvartiri + "&BlockCMS=on&user=admin&pwd=admin"   
    bot.send_message(message.from_user.id, URL1)


#def version_beward(message):
 #   global URL_GET
  #  global ip_adrr
   # ip_addr= message.text
 #   URL_GET = "http://" + ip_addr + "/cgi-bin/systeminfo_cgi?action=get"
  #  headers = {
   #         'Authorization': 'Basic YWRtaW46YWRtaW4=',
    #        'Content-Type': 'application/json'
     #   }
    #response = requests.request("GET", URL_GET, headers=headers, timeout=1)
    #line = response.text
    #print(line)

bot.polling()
