from celery import shared_task
from config import settings
import datetime
import requests

from habits.models import Habits



@shared_task
def send_notification():
    token = settings.TOKEN_BOT
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    now = datetime.datetime.now()
    habit = Habits.objects.all()

    for habit_item in habit:
        print("Бот запускается")
        if now.time() <= habit_item.time:
            print("УРАА")
            requests.post(url,
                          data={"chat_id": habit_item.owner.chat_id,
                                "text": f'В {habit_item.time} часов вы должны {habit_item.action} в {habit_item.place}'}
                          )
