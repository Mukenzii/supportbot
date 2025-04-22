code_template = """
import telebot

TOKEN = "YOUR_BOT_TOKEN"  # Замени на свой токен
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def handle_messages(message):
    if "привет" in message.text.lower():
        bot.reply_to(message, "Привет! Добро пожаловать в Startup House! 🚀")
    elif "ии" in message.text.lower() or "бизнес" in message.text.lower():
        bot.reply_to(message, "Интересная тема! Расскажи, как ты используешь ИИ в бизнесе? 💡")

bot.infinity_polling()
"""

connect_openai = """Вот пошаговая инструкция, как подключить OpenAI API к Telegram-боту, чтобы он отвечал с помощью ChatGPT:
1.OpenAI API ключ — получи здесь: https://platform.openai.com/account/api-keys
2.Установи нужные библиотеки: pip install openai pyTelegramBotAPI"""

github_links = """Вот простые телеграм-боты от Github:
1.https://github.com/eternnoir/pyTelegramBotAPI/blob/master/examples/echo_bot.py
2.https://github.com/eternnoir/pyTelegramBotAPI/blob/master/examples/step_example.py
3.https://github.com/eternnoir/pyTelegramBotAPI/blob/master/examples/detailed_example/detailed_example.py"""

