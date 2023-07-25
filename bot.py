from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
import os
from dotenv import load_dotenv

# python-telegram-bot==13.7.0 версия

# Токен
load_dotenv()  # Загрузка переменных окружения из файла .env
TOKEN = os.getenv("TOKEN")

# аудио
SQL_MP3_FILE = "SQL.mp3"
LOVE_MP3_FILE = "love.mp3"
ABOUT_MP3_FILE = "about.mp3"
GPT_MP3_FILE = "about.mp3"

# Старт
def start(update: Update, _: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_text(f"Привет, {user.first_name}! Привет Я бот Игоря П. Вот его фото")
    update.message.reply_photo(photo=open("img1.jpg", "rb"))
    update.message.reply_photo(photo=open("img2.jpg", "rb"))

    # кнопки
    buttons = [
        [KeyboardButton("SQL"), KeyboardButton("love")],
        [KeyboardButton("Git"), KeyboardButton("О авторе")]
    ]
    keyboard = ReplyKeyboardMarkup(buttons, one_time_keyboard=True)
    update.message.reply_text("Что вы хотите узнать?", reply_markup=keyboard)

# Обработчик кнопки SQL
def play_sql_audio(update: Update, _: CallbackContext) -> None:
    update.message.reply_audio(audio=open(SQL_MP3_FILE, "rb"))

# Обработчик кнопки Love
def play_love_audio(update: Update, _: CallbackContext) -> None:
    update.message.reply_audio(audio=open(LOVE_MP3_FILE, "rb"))

# Обработчик кнопки Git
def git_link(update: Update, _: CallbackContext) -> None:
    git_repo_link = "https://github.com/Perekalskiyigor/bot_forYandex.git"
    update.message.reply_text(f"Я программист на большом заводе. Программирую всякие разные штуки,: {git_repo_link}")

# Обработчик кнопки О авторе
def about_author(update: Update, _: CallbackContext) -> None:
    update.message.reply_audio(audio=open(ABOUT_MP3_FILE, "rb"))

# Обработчик команды /GPTAbout
def gpt_about(update: Update, _: CallbackContext) -> None:
    update.message.reply_audio(audio=open(GPT_MP3_FILE, "rb"))

def main() -> None:
    updater = Updater(TOKEN)

    # Диспетчер
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start)) # start
    dispatcher.add_handler(MessageHandler(Filters.regex('^(SQL)$'), play_sql_audio)) # SQL
    dispatcher.add_handler(MessageHandler(Filters.regex('^(love)$'), play_love_audio)) # love
    dispatcher.add_handler(MessageHandler(Filters.regex('^(Git)$'), git_link)) # git
    dispatcher.add_handler(MessageHandler(Filters.regex('^(О авторе)$'), about_author)) # О авторе
    dispatcher.add_handler(CommandHandler("GPTAbout", gpt_about)) # /GPTAbout
    updater.start_polling()

if __name__ == "__main__":
    main()
