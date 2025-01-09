import requests
import telebot
import json

telegram_token = '7804132046:AAENrVW8Z5qwaJ7fFMWqo6nBsV-rLhLzFHI'
weather_token = '5779cbdb104b00473fb6f0ab80598a6f'

bot = telebot.TeleBot(token = telegram_token)


@bot.message_handler(commands=["start"])
def start_command(message):
    bot.send_message(message.chat.id, "Привет! Напиши мне название города, и я пришлю сводку погоды.")

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        bot.reply_to(message, f'Сейчас температура воздуха: {data ["main"]["temp"]} ˚С, скорость ветра: {data ["wind"]["speed"]} м/с, влажность воздуха: {data ["main"]["humidity"]} %')
    else: bot.reply_to(message, 'Пожалуйста, напиши корректное название города')




bot.polling(non_stop = True)
