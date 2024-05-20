from habits.apps import HabitsConfig
from django.urls import path
from habits.views import HabitCreateView,HabitListView,HabitRetrieveVIew,HabitUpdateView,HabitDestroyView

app_name = HabitsConfig.name

urlpatterns = [
    path('create',HabitCreateView.as_view(),name='habit_create'),
    path('',HabitListView.as_view(),name='habits_list'),
    path('view/<int:pk>',HabitRetrieveVIew.as_view(),name='habit_view'),
    path('edit/<int:pk>',HabitUpdateView.as_view(),name='habit_edit'),
    path('delete/<int:pk>',HabitDestroyView.as_view(),name='habit_delete'),
]