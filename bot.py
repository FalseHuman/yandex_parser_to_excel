import telebot, logging, time, yandex_parser, os
from telebot import types
from config import token

logging.basicConfig(format='%(asctime)s %(levelname)s - %(message)s',
                    level=logging.INFO, filename='bot.log')

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    print('start')
    bot.send_message(message.chat.id, 'Добро пожаловать в бота, чтобы получить файл введите ссылку на товар с Яндекс.Маркета если возникли вопросы, пишите в лс - @FalseHuman. Например, https://market.yandex.ru/product--navigator-navitel-g500/13624884?nid=27021910')

@bot.message_handler(content_types=['text'])
def message(message):
    if 'market.yandex' in message.text:
        bot.send_message(message.chat.id, 'Запускаю парсинг, примерное время формирования файла от 5 минут 🧭')
        yandex_parser.start_parser(message.chat.id, message.text)
    else:
        bot.send_message(message.chat.id, 'Введите корректную ссылку с Яндекс.Маркета')


while True:
    try:
        bot.polling(none_stop=True)  # Это нужно чтобы бот работал всё время
    except:
        time.sleep(5)  # если ошибка бот уходит в спящий режим на 5 секунд