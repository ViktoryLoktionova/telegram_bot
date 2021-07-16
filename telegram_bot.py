import telebot
from pyowm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('1da0962b4d2c9e728ac17a3ddd7a188a')
bot = telebot.TeleBot("1869771840:AAGDFqBCTfMW_yHYZJyINaxz4hS-qRuV3s4", parse_mode = None)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    #print(w.wind()['speed'], w.temperature('celsius')['temp'])
    weather_info = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
    weather_info += "Температура: " + str(w.temperature('celsius')['temp']) + "\n"
    weather_info += "Скорость ветра: " + str(w.wind()['speed']) + " м/с" + "\n"
    bot.reply_to(message, weather_info)

bot.polling()