from celery import shared_task
from django.conf import settings
import datetime
import requests

from habits.models import Habits
import json


@shared_task
def send_notification():
    token = settings.TOKEN_BOT
    url = f"https://api.telegram.org/bot{token}/"
    now = datetime.datetime.now()
    habit = Habits.objects.all()
    for habit_item in habit:
        if now.time() <= habit_item.time:
            print("Бот запустился")
            data = requests.get(url + "getupdates")
            data1 = json.loads(data.content)
            chat_id = data1["result"][0]["message"]["chat"]["id"]
            requests.post(url+"sendMessage",
                          data={"chat_id": chat_id,
                                "text": f'В {habit_item.time} часов вы должны {habit_item.action} в {habit_item.place}'}
                          )
