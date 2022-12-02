import telebot 
bot = telebot.TeleBot("5875338816:AAF623-eAg_6qbkZFnnLv5eEipzDjTjvhvs", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

bot.infinity_polling()