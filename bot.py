
from webbrowser import get
import telebot;
from getTask import * 

bot = telebot.TeleBot('5111904045:AAEDPZLqKaacz7BFQV9Aohjj-5gmjEmoUCA');


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    splitted_text = str(message.text).lower().split()
    if str(message.text).lower() == "привет":
        bot.send_message(message.from_user.id, "Привет, это проект Physicsfights - Многофункциональный сервис для изучения физики. \n Для информации введите /help.")
    elif str(message.text).lower() == "/help":
        bot.send_message(message.from_user.id, "проект Physicsfights - Многофункциональный сервис для изучения физики \n Список команд: \n /s - вывести свой рейтинг \n /t - Получить задачу\n /a - ответ - дать ответ на задачу")
    elif splitted_text[0] == "/t":
        task, ans, taskid = getTask(message.from_user.id)
        bot.send_message(message.from_user.id, task)    
    elif splitted_text[0] == "/a":
        task, ans, taskid = getTask(message.from_user.id)
        str1="Ответ не верный"
        if CheckAns(message.from_user.id,taskid, splitted_text[1]):
            str1="Ответ верный"
        bot.send_message(message.from_user.id, str1)
    elif splitted_text[0] == "/s":
        score = getScore(message.from_user.id)
        bot.send_message(message.from_user.id, "Ваш рейтинг: "+ str(score))   
    else:
        bot.send_message(message.from_user.id, "Для информации введите /help.")

bot.polling(none_stop=True, interval=0)