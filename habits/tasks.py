from celery import shared_task
import telebot
from django.conf import settings
from telebot import types


@shared_task
def send_notification(habit):

    bot=telebot.TeleBot(settings.TOKEN_BOT)
    print("Бот запускается")
    @bot.message_handler(commands=["start"])
    def main(message):
        bot.send_message(message.chat.id, f'Привет, {message.from_user.username}')
        bot.send_message(message.chat.id, f'Введите "/habit" для просмотра привычки')

    @bot.message_handler(commands=["habit"])
    def notification(message):
        bot.send_message(message.chat.id,f'Вы должны {habit.action} в {habit.time} в {habit.place} и должны это повторить не меньше,чем {habit.periodicity} раз в неделю ')
        bot.send_message(message.chat.id, f'Напишите слово привычка,если не знаете что такое {habit.action}')
    @bot.message_handler()
    def func(message):
        if message.text.lower() == "привычка":
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("что это",url=f'https://www.google.com/search?q={habit.action}'))
            bot.reply_to(message, "В ссылке можно посмотреть что это", reply_markup=markup)

        else:
            bot.send_message(message.chat.id, 'Кроме слово "привычка" ничего не знаю')

    bot.infinity_polling()