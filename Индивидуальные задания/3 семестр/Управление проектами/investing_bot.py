import telebot
import requests
from telebot import types
from bs4 import BeautifulSoup
from time import sleep

sleep(3)

url_GAZP = 'https://ru.investing.com/equities/gazprom_rts'
url_TCSG = 'https://ru.investing.com/equities/tcs-group-holding-plc?cid=1153662'
url_VTBR = 'https://ru.investing.com/equities/vtb_rts'

response_1 = requests.get(url_GAZP)
response_2 = requests.get(url_TCSG)
response_3 = requests.get(url_VTBR)

soup_1 = BeautifulSoup(response_1.text, "lxml")
soup_2 = BeautifulSoup(response_2.text, "lxml")
soup_3 = BeautifulSoup(response_3.text, "lxml")

data_1 = soup_1.find('span', class_='text-2xl').text
data_2 = soup_2.find('span', class_='text-2xl').text
data_3 = soup_3.find('span', class_='text-2xl').text

# print(data_1 + '₽')
# print(data_2 + '₽')
# print(data_3 + '₽')

TOKEN = '5731688722:AAEJNwdtoLeuhLVNisK5Sx5t56FCAUKWQ7A'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton('Цены акций')

    markup.add(item)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Цены акций':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('GAZP · Газпром')
            item2 = types.KeyboardButton('TCSG · Тинькофф Банк')
            item3 = types.KeyboardButton('VTBR · Банк ВТБ')
            back = types.KeyboardButton('Выйти')
            markup.add(item1, item2, item3, back)

            bot.send_message(message.chat.id, 'Цены акций:', reply_markup=markup)

        elif message.text == 'GAZP · Газпром':

            bot.send_message(message.chat.id, f'GAZP · Газпром: \n{data_1}₽')

        elif message.text == 'TCSG · Тинькофф Банк':

            bot.send_message(message.chat.id, f'TCSG · Тинькофф Банк: \n{data_2}₽')

        elif message.text == 'VTBR · Банк ВТБ':

            bot.send_message(message.chat.id, f'VTBR · Банк ВТБ: \n{data_3}₽')

        elif message.text == 'Выйти':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Цены акций')

            markup.add(item1)

            bot.send_message(message.chat.id, 'Печалька 😭', reply_markup=markup)

        else:

            bot.send_message(message.chat.id, f'Воспользуйтесь командой: /help')


bot.polling(none_stop=True)