# -*- coding: utf8 -*-
import telebot
from telebot import types

bot = telebot.TeleBot('1642909297:AAFMhkjg1TJr4qCJltG3_wxhXPctt0uaCXg')

def main():
    markup = types.ReplyKeyboardMarkup(True)
    key1 = types.KeyboardButton('Заткнииииись')
    key2 = types.KeyboardButton('Анекдотик')
    key3 = types.KeyboardButton('Вася урод моральный')
    markup.add(key1)
    markup.add(key2)
    markup.add(key3)
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет', reply_markup=main())

@bot.message_handler(content_types=['text'])
def cont(message):
    if message.text == 'Заткнииииись':
        bot.send_message(message.chat.id, 'Ты что тут на кнопки тыкаешь,а, быдло?', reply_markup=main())
        audio = open(r'cum.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
        audio.close()
    elif message.text == 'Анекдотик':
        bot.send_message(message.chat.id, 'Джимми вскакивает с постели и радостно забегает на второй этаж к отцу, в его кабинет. "Папа! Папа, сколько мне ле–е–е–ет!?" — забегая в комнату кричит ребенок."Тебе — восемь!" — подыгрывая сыну выкрикивает отец. "Пра–а–а–авильно!" отвечает Джимми и выбегает из комнаты."Дедешка!" — кричит Джимми спускаясь по лестнице в гостинную. "Ско–о–олько мне лет?!".Мудрый дедушка сидящий у камина откладывает в сторону газету и недавно зажжённую трубку. "Подойди–ка ближе, Джимми" — сказал дедушка.Джимми вприпрыжку подбежал к дедушке. Дедушка запускает свою руку в штанишки Джимми и резко хватает его член, после чего ослабляет хватку и начинает водить своей рукой вниз и вверх. Несколько ритмичных движений и дедушка проводит указательным пальцем по промежности Джимми и останавливается на его анусе. После круговых движений вокруг анального отверстия дедушка проникает указательным пальцем внутрь.Затем дедушка снова проводит пальцем по промежности внука, только в обратном направлении и заканчивает все это действо крепко сжав кончик пениса Джимми.От подобных действий Джимми вскрикивает. "Тебе восемь" — заявил дедушка. "Но как ты узнал?" — спросил Джимми. "Я услышал как ты сказал своему отцу"',reply_markup=main())
    elif message.text == 'Вася урод моральный':
        bot.send_message(message.chat.id, 'Ты реально урод, я тебя ненавижу', reply_markup=main())
bot.polling() 
