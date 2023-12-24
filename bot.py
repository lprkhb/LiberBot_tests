import telebot


Token = ''


@bot.message_handler(commands=['start'])
def start_page(message):
    pass


@bot.message_handler(func=lambda message: True)
def send_message(message):
    bot.send_message(message.chat.id, "")
    return


if __name__ = __main__:
   bot = telebot.TeleBot(f"{Token}")
   bot.polling(none_stop=True)