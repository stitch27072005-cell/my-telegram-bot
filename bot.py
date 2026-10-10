import telebot
import random

# Вставь сюда свой токен вместо "8829910255:AAF5L3UaOl2Qe9lVB0u6rriE7e0deV0A4GU"
TOKEN = "8829910255:AAF5L3UaOl2Qe9lVB0u6rriE7e0deV0A4GU"
bot = telebot.TeleBot(TOKEN)

# Список мотивирующих комплиментов
compliments = [
    "Ты справляешься лучше, чем думаешь!",
    "У тебя потрясающая сила воли!",
    "Сегодня ты сделал(а) шаг вперёд — это уже победа!",
    "Ты достоин(на) всего самого лучшего!",
    "Твоя энергия заразительна — продолжай в том же духе!",
    "Ты умнее и сильнее, чем тебе кажется!",
    "Каждый день с тобой мир становится чуть лучше!",
    "Ты уже прошёл(ла) через многое — и стал(а) ещё круче!",
    "Верь в себя так же сильно, как я верю в тебя!",
    "Ты — настоящий боец. Горжусь тобой!"
]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 
        "Привет! Я Motivational Compliment Bot\n\n"
        "Я здесь, чтобы поднимать тебе настроение и напоминать, какой ты классный!\n\n"
        "Напиши /help чтобы увидеть команды.")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message,
        "Доступные команды:\n"
        "/start — приветствие\n"
        "/help — эта справка\n"
        "/compliment — получить случайный мотивирующий комплимент")

@bot.message_handler(commands=['compliment'])
def send_compliment(message):
    compliment = random.choice(compliments)
    bot.reply_to(message, compliment)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    compliment = random.choice(compliments)
    bot.reply_to(message, f"Я рядом и верю в тебя!\n\n{compliment}")

print("Бот запущен... Нажми Ctrl+C чтобы остановить")
bot.infinity_polling()