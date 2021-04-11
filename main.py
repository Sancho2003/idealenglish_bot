import telebot

bot = telebot.TeleBot('1601838792:AAFCSBGDVasuRk10nWDZYcZ9nz5noB-GqtM')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id, 'Привет, чем могу помочь?')
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Напиши привет')
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю, напиши /help')


bot.polling(none_stop=True, interval=0)
