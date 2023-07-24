import logging
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler

# python-telegram-bot==13.7.0 версия


# Токен
TOKEN = "5947542394:AAGKFymHjLa--3bMz2QF8q-CP-EgfdWyKEE"

# аудио
SQL_MP3_FILE = "SQL.mp3"
LOVE_MP3_FILE = "Love.mp3"

# Старт
def start(update: Update, _: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_text(f"Привет, {user.first_name}! Я бот с двумя фотографиями.")
    update.message.reply_photo(photo=open("img1.jpg", "rb"))
    update.message.reply_photo(photo=open("img2.jpg", "rb"))

 #кнопки
    buttons = [
        [KeyboardButton("SQL"), KeyboardButton("Love")],
        [KeyboardButton("Git")]
    ]
    keyboard = ReplyKeyboardMarkup(buttons, one_time_keyboard=True)
    update.message.reply_text("Что вы хотите узнать?", reply_markup=keyboard)

# Обработчик кнопки SQL
def play_sql_audio(update: Update, _: CallbackContext) -> None:
    update.message.reply_audio(audio=open(SQL_MP3_FILE, "rb"))

# Обрабочик кнопки Love
def play_love_audio(update: Update, _: CallbackContext) -> None:
    update.message.reply_audio(audio=open(LOVE_MP3_FILE, "rb"))

# Обработчик кнопки Git
def git_link(update: Update, _: CallbackContext) -> None:
    git_repo_link = "https://github.com/Perekalskiyigor/bot_forYandex.git"
    update.message.reply_text(f"Ссылка на Git репозиторий: {git_repo_link}")

def main() -> None:
    updater = Updater(TOKEN)

# Диспетчер
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start)) # start
    dispatcher.add_handler(CallbackQueryHandler(play_sql_audio, pattern='sql')) #sql
    dispatcher.add_handler(CallbackQueryHandler(play_love_audio, pattern='love')) # love
    dispatcher.add_handler(MessageHandler(Filters.regex('^(Git)$'), git_link)) # git
    updater.start_polling()

if __name__ == "__main__":
    main()
