import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "Привет! Я учебный Telegram бот. Напиши /help, чтобы узнать доступные команды."
    )


@bot.message_handler(commands=["help"])
def help_command(message):
    bot.reply_to(
        message,
        "Доступные команды:\n"
        "/start — запустить бота\n"
        "/help — показать список команд"
    )


bot.infinity_polling()