from rest_framework.serializers import ValidationError

from habits.models import Habits



class ChoiceValidator:
    def __init__(self,field1,field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self):
        habit = Habits.objects.all()
        if habit.related_habit and habit.reward:
            raise ValidationError('Нельзя заполнять одновременно и поле вознаграждения, и поле связанной привычки')

class TimeCompleteValidator:
    def __init__(self,field):
        self.field = field

    def __call__(self):
        habit = Habits.objects.all()
        if habit.time_to_complete > 120:
            raise ValidationError('Время выполнения должно быть не больше 120 секунд')


class RelatedPleasantValidator:
    def __init__(self,field1,field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self):
        habit = Habits.objects.all()
        if habit.related_habit:
            if not habit.is_pleasant_habit:
                raise ValidationError('В связанные привычки могут попадать только привычки с признаком приятной привычки')


class PleasantValidator:
    def __init__(self, field1, field2,field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def __call__(self):
        habit = Habits.objects.all()
        if habit.is_pleasant_habit:
            if habit.reward or habit.related_habit:
                raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки')



class PeriodicityValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self):
        habit = Habits.objects.all()
        if habit.periodicity < 1 or habit.periodicity > 7:
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')