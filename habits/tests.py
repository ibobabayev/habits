from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User
from habits.models import Habits


class HabitsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='test1@mail.com',
            password='123'
        )
        self.client.force_authenticate(user=self.user)

        self.habit = Habits.objects.create(
            owner=self.user,
            place='дома',
            time="20:00:00",
            action='читать книгу',
            is_pleasant_habit=False,
            related_habit=None,
            periodicity=5,
            reward='покушать блинчики',
            time_to_complete=60,
            is_public=True
        )

    def test_create_habit(self):
        """ Тестирование на создание полезной привычки"""

        data = {
            "owner": self.user.id,
            "place": 'дома',
            "time": "20:00:00",
            "action": 'читать книгу',
            "is_pleasant_habit": False,
            "related_habit": "",
            "periodicity": 5,
            "reward": "покушать блинчики",
            "time_to_complete": 60,
            "is_public": True
        }
        response = self.client.post(
            '/habits/create', data=data
        )
        print('RESPONSE', response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Habits.objects.all().exists())

    def test_list_habit(self):
        """Тестирование на вывод списка полезных привычек"""
        response = self.client.get(
            '/habits/'
        )
        print('RESPONSE', response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"count": 1, "next": None, "previous": None, "results": [
            {'id': self.habit.id, 'place': 'дома', 'time': '20:00:00', 'action': 'читать книгу',
             'is_pleasant_habit': False, 'periodicity': 5, 'reward': 'покушать блинчики',
             'time_to_complete': 60, 'is_public': True, 'owner': self.user.pk, 'related_habit': None}
        ]}
                         )

    def test_detail_habit(self):
        """Тестирование на вывод одной привычки"""
        data = {
            "owner": self.user.id,
            "place": 'дома',
            "time": "20:00:00",
            "action": 'читать книгу',
            "is_pleasant_habit": False,
            "related_habit": "",
            "periodicity": 5,
            "reward": "покушать блинчики",
            "time_to_complete": 60,
            "is_public": True
        }
        response = self.client.get(
            f'/habits/view/{self.habit.id}',
            data=data
        )
        print('RESPONSE', response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_habit(self):
        """Тестирование на обновление или изменения привычки"""
        data = {
            "owner": self.user.id,
            "place": 'караоке',
            "time": "23:00:00",
            "action": 'спеть песню',
            "is_pleasant_habit": True,
            "related_habit": "",
            "periodicity": 3,
            "reward": "",
            "time_to_complete": 90,
            "is_public": False
        }
        response = self.client.patch(
            f'/habits/edit/{self.habit.id}',
            data=data
        )
        print('RESPONSE', response.json())

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.habit.refresh_from_db()
        self.assertEqual(self.habit.place, data["place"])
        self.assertEqual(self.habit.action, data["action"])

    def test_delete_habit(self):
        """Тестирование на удаление привычки"""
        data = {
            "owner": self.user.id,
            "place": 'караоке',
            "time": "23:00:00",
            "action": 'спеть песню',
            "is_pleasant_habit": True,
            "related_habit": "",
            "periodicity": 3,
            "reward": "",
            "time_to_complete": 90,
            "is_public": False
        }
        response = self.client.delete(
            f'/habits/delete/{self.habit.id}',
            data=data
        )
        print('RESPONSE', response.content)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
