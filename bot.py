
from webbrowser import get
import telebot;
from genQoute import genQoute 

bot = telebot.TeleBot('5111904045:AAGAzpDoyX86hX2pnc_ad4CilZp-G5x7sQw');


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    splitted_text = str(message.text).lower().split()
    if str(message.text).lower() == "привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь? Для информации введите /help.")
    elif str(message.text).lower() == "/help":
        bot.send_message(message.from_user.id, "Список команд: /q - \{текст для анализа\}  - Подобрать цитату ")
    elif splitted_text[0] == "/q":
        bot.send_message(message.from_user.id, genQoute(splitted_text[1]))
    else:
        bot.send_message(message.from_user.id, "Для информации введите /help.")

bot.polling(none_stop=True, interval=0)