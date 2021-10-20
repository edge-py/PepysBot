from imports import *

bot = tb.TeleBot(BOT_KEY)

@bot.message_handler(commands=["старт", "с", "s", "start"])
def send_welcome(message):
	bot.send_message(chat_id = message.from_user.id, text="Введи 'цыпленок' или 'утенок':")

@bot.message_handler(regexp='цып')
def send_photo(message):
    rand_pic_number = randint(1,3)
    bot.send_photo(chat_id = message.from_user.id, photo = ph_chick_list[rand_pic_number])
    bot.send_message(chat_id = message.from_user.id, text=
    """
    Введи 'цыпленок' или 'утенок':
    /help - помощь
    """)
    markup = types.ReplyKeyboardMarkup()
    markup.add('цыпленок', 'утенок') #Имена кнопок

@bot.message_handler(regexp='ут')
def send_photo(message):
    rand_pic_number = randint(1,3)
    bot.send_photo(chat_id = message.from_user.id, photo = ph_duck_list[rand_pic_number])
    bot.send_message(chat_id = message.from_user.id, text=
    """
    Введи 'цыпленок' или 'утенок':
    /help - помощь
    """)
    markup = types.ReplyKeyboardMarkup()
    markup.add('цыпленок', 'утенок') #Имена кнопок

@bot.message_handler(commands=['помощь', 'п', 'help', 'h'])
def send_message(message):
    bot.send_message(chat_id = message.from_user.id,text = """
    Доступные команды:
    /start (/старт) - Начать работу с @Pepys_Bot
    /help (/помощь) - Список доступных команд

    /secret - пажилой крол
    """)
    markup = types.KeyboardButton

@bot.message_handler(commands='secret')
def send_photo(message):
    bot.send_photo(chat_id = message.from_user.id, photo = 'https://sun9-66.userapi.com/impg/z0NbvgiSDMOEP2NKlFP2X1DD_kc-03DkcoWSaA/boJMiTtj6ug.jpg?size=600x600&quality=96&sign=c1ee86ecc869788dfb60dabdf6626b3c&type=album')

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, "Неопознанная команда, введи /help или /помощь чтобы увидеть список доступных команд.")

bot.infinity_polling()