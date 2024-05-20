from rest_framework.test import APITestCase , APIClient
from rest_framework import status
from users.models import User
from habits.models import Habits

class HabitsTestCase(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            email='test1@mail.com',
            password = '123'
        )
        self.user2 = User.objects.create(
            email='test2@mail.com',
            password='123'
        )

        self.client.force_authenticate(user=self.user1)
        self.client.force_authenticate(user=self.user2)


        self.useful_habit = Habits.objects.create(
            owner=self.user1,
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
        self.pleasant_habit = Habits.objects.create(
            owner=self.user2,
            place='караоке',
            time="22:00:00",
            action='спеть песню',
            is_pleasant_habit=True,
            related_habit=None,
            periodicity=2,
            reward="",
            time_to_complete=100,
            is_public=False
        )

    def test_useful_habit(self):
        """ Тестирование на создание полезной привычки"""

        data = {
            "owner" : self.user1,
            "place" : 'дома',
            "time" : "20:00:00",
            "action" : 'читать книгу',
            "is_pleasant_habit" : False,
            "related_habit" : "",
            "periodicity" : 5,
            "reward" : "покушать блинчики",
            "time_to_complete" : 60,
            "is_public" : True
        }
        response = self.client.post(
            'habits/create',data=data
        )
        print('RESPONSE',response.content)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertTrue(Habits.objects.all().exists())

    # def test_list_useful(self):
    #     """Тестирование на вывод списка полезных привычек"""
    #     response = self.client.get(
    #         'habits/'
    #     )
    #     self.assertEqual(response.status_code,status.HTTP_200_OK)
        # self.assertEqual(response.json(),)


    def test_pleasant_habit(self):
        """ Тестирование на создание приятной привычки"""

        data = {
            "owner" : self.user2,
            "place" : 'караоке',
            "time" : "22:00:00",
            "action" : 'спеть песню',
            "is_pleasant_habit" : True,
            "related_habit" : '',
            "periodicity" : 2,
            "reward" : "",
            "time_to_complete" : 100,
            "is_public" : False
        }
        response = self.client.post(
            'habits/create',data=data
        )
        print('RESPONSE', response.content)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertTrue(Habits.objects.all().exists())

    # def test_list_pleasant(self):
    #     """Тестирование на вывод списка приятных привычек"""
    #     response = self.client.get(
    #         'habits/'
    #     )
    #     self.assertEqual(response.status_code,status.HTTP_200_OK)
        # self.assertEqual(response.json(),)