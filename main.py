import telebot
import bot_keyboards

print()

bot = telebot.TeleBot('6918942734:AAFrH47noFlQ7c6U4B4-MTSbZmGOYIJ-UH0')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.from_user.username:
        match message.text:
            case "/start":
                bot.send_message(message.from_user.id, text='Добро', reply_markup=bot_keyboards.keyboard1)

    else:
        bot.send_message(message.from_user.id, text='Упс! Кажется у вас не уставновлено имя пользвоателя! Это обязательный пункт для функционирвоания бота!')



@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    match call.data:
        case "to_find":
            bot.send_message(call.message.chat.id, 'penis')


bot.polling(none_stop=True, interval=0)