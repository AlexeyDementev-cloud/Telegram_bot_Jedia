#Libraries
import telebot;
from tkinter import *
from tkinter.ttk import *
from time import strftime
import requests
from bs4 import BeautifulSoup

# API telegram
bot = telebot.TeleBot('#Put your api here');
@bot.message_handler(content_types=['text'])






#Main commands

def get_text_messages(message):
    # Function for weather
    def check_weather(city):
  
        headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36Vj'
        }

        responce = requests.get(f'https://www.google.com/search?q=погода+в+{city}', headers=headers)

        soup = BeautifulSoup(responce.text, 'html.parser')
        temperature = soup.select('#wob_tm')[0].getText()
        humidity = soup.select('#wob_hm')[0].getText()
        wind = soup.select('#wob_ws')[0].getText()
        bot.send_message(message.from_user.id, 'In moscow now:')
        bot.send_message(message.from_user.id, f'🌡️: {temperature}C')
        bot.send_message(message.from_user.id, f'💧: {humidity}')
        bot.send_message(message.from_user.id, f'🌬️: {wind}')


    # Function of time
    def real_clock():
        i = ()
        string = strftime('%H : %M')
        p = int(strftime('%H'))

        if p > 6:
            i = 'Good night!' 
        elif p > 12:
            i = 'Good morning!' 
        elif p > 15:
            i ='Good afternoon!' 
        elif p > 21:
            i = 'Good evening!'
        else:
            i = 'Good night!'
        bot.send_message(message.from_user.id, string)
        bot.send_message(message.from_user.id, i)



#Some non reason Function 
    # Hello
    if message.text == 'Hello' or message.text == '/help' or message.text == '/restart' or message.text == '/start' :
        bot.send_message(message.from_user.id, 'Hi, Im a Jedia 0.11b assistant bot. So far I can tell you the time, weather and schedule for the week, but soon there will be more functionality!')       
    # Time
    elif message.text == 'time' or message.text == 'Time':
        real_clock()
    # Easter egg special for my friend
    elif message.text == 'Улыбнись' or message.text == 'улыбнись':
        bot.send_message(message.from_user.id, 'Мне лень')
    elif message.text == ':(':
        bot.send_message(message.from_user.id, 'Кто грустит, у того попа не будет расти')
    elif message.text == 'Число пи' or message.text == 'число пи': 
        bot.send_message(message.from_user.id, '3,14здуй отсюда. Заебали вы меня') 
    # Weather
    elif message.text == 'Weather' or message.text == 'weather':
        check_weather('Москва')
    # Eror
    else:
        bot.send_message(message.from_user.id, 'I dont understand u. Please write /help.')













bot.polling(none_stop=True, interval=0)