from rest_framework import generics
from habits.models import Habits
from habits.serializer import HabitsSerializer
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from users.permissions import IsOwner
from habits.pagination import HabitPagination


class HabitCreateView(generics.CreateAPIView):
    """ Эндпоинт для создания привычки"""
    serializer_class = HabitsSerializer
    # permission_classes = [IsAuthenticated]

class HabitListView(generics.ListAPIView):
    """ Эндпоинт для вывода списка привычек"""
    serializer_class = HabitsSerializer
    permission_classes = [IsAdminUser]
    pagination_class = HabitPagination

    def get_queryset(self):
        user = self.request.user
        if not user.is_superuser:
            queryset = Habits.objects.filter(owner=user)
        else:
            queryset = Habits.objects.all()
        return queryset

class HabitRetrieveVIew(generics.RetrieveAPIView):
    """ Эндпоинт для просмотра одной привычки"""
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsAdminUser,IsOwner]

class HabitUpdateView(generics.UpdateAPIView):
    """ Эндпоинт для обновления или изменения привычки"""
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsAdminUser,IsOwner]


class HabitDestroyView(generics.DestroyAPIView):
    """ Эндпоинт для удаления привычки"""
    queryset = Habits.objects.all()
    permission_classes = [IsAdminUser,IsOwner]
