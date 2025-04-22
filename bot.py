from telebot import TeleBot
from telebot.types import Message
from sources import *


BOT_API = '8086302490:AAFSGxyr13fNppCUufQbzv9Gism7hyNyiRU'
bot = TeleBot(BOT_API)


@bot.message_handler(commands=['start'])
def reaction_start(message: Message):
    chat_id = message.chat.id

    bot.send_message(chat_id,
                     'Здравствуйте, я бот, который поможет вам выполнить это тестовое задание. Чем я могу вам помочь?')

@bot.message_handler(content_types=['text'])
def reaction_text(message: Message):
    chat_id = message.chat.id
    if 'привет' in message.text.lower():
        bot.send_message(chat_id, "Привет! Добро пожаловать в Startup House! 🚀")

    elif 'чём суть задания' in message.text.lower() or 'что надо делать?' in message.text.lower():
        bot.send_message(chat_id,
                         'Ты должен создать Telegram-бота, который реагирует на текст в чате. Я могу подсказать, как его реализовать')

    elif "как создать бота" in message.text.lower():
        bot.send_message(chat_id, 'Открой Telegram и напиши @BotFather → /newbot → дай имя и юзернейм.')

    elif "есть пример кода?" in message.text.lower():
        bot.send_message(chat_id, code_template)

    elif "почему бот не отвечает?" in message.text.lower():
        bot.send_message(chat_id, "Проверь: 1) Токен верный? 2) Подписан ли ты на бота? 3) Есть ли polling?")

    elif "у меня не получается" in message.text.lower() or "не получается" in message.text.lower():
        bot.send_message(chat_id, "Ты справишься! 💪 Даже маленький шаг — это прогресс")

    elif "когда дедлайн?" in message.text.lower():
        bot.send_message(chat_id, "Ты должен сдать бота в течение 3 дней с момента получения задания")

    elif "подключение openai" in message.text.lower():
        bot.send_message(chat_id, connect_openai)

    elif "пример с github" in message.text.lower() or "github линк" in message.text.lower():
        bot.send_message(chat_id, github_links)


if __name__ == '__main__':
    bot.infinity_polling()