import telebot

from settings import API_KEY

bot = telebot.TeleBot(API_KEY)

'''
Функция, отвечает на вызов команды /start, обратите внимание это не
content_types, а (commands=['start'])
'''
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Вызван /start')

'''
Функция принимает сообщение и отвечает сообщением, content_types=['text']
'''
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'Привет':
        bot.send_message(message.chat.id, 'Привет')
    elif message.text.lower() == 'Пока':
        bot.send_message(message.chat.id, 'Пока')
    elif message.text.lower() == 'я люблю тебя':
    	bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAANaXlt720mSKQFAoLbH2w3ge40JRasAAusCAALz474LOyVmE-ATWsMYBA')

'''
Функция принимает стикер и отвечает стикером, content_types=['sticker']
'''
@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)
# sorry за PEP8

bot.polling()