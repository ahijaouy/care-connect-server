from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Caretaker(models.Model):
    """ Model for a Caretaker """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=70, blank=False)

    def __str__(self):
        return self.name


class Elderly(models.Model):
    """ Model for an Elderly """
    name = models.TextField(max_length=70, blank=False)
    birth_date = models.DateField()
    picture = models.TextField(blank=True)

    def __str__(self):
        return self.name


class FamilyMember(models.Model):
    """ Model for a Family Member """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=70, blank=False)
    elderly = models.OneToOneField(Elderly, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ActivityType(models.Model):
    name = models.TextField(max_length=70, blank=False)
    description = models.TextField(max_length=250, blank=False)
    img_url = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Activity(models.Model):
    activityType = models.ForeignKey(ActivityType, on_delete=models.CASCADE)
    elderly = models.ForeignKey(Elderly, on_delete=models.CASCADE)
    caretaker = models.ForeignKey(Caretaker, on_delete=models.CASCADE)
    duration = models.DurationField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return (str(self.activityType) + " by " + str(self.elderly) + " on "
                + self.date.strftime("%Y-%m-%d %H:%M:%S"))


class Comment(models.Model):
    elderly = models.ForeignKey(Elderly, on_delete=models.CASCADE)
    caretaker = models.ForeignKey(Caretaker, on_delete=models.CASCADE)
    note = models.TextField(max_length=250, blank=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.note[:10] + "..."


class QuizResponse(models.Model):
    elderly = models.ForeignKey(Elderly, on_delete=models.CASCADE)
    caretaker = models.ForeignKey(Caretaker, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    q1_attentive = models.BooleanField(default=True)
    q2_hope = models.BooleanField(default=True)
    q3_empathetic = models.BooleanField(default=True)
    q4_humor = models.BooleanField(default=True)
    q5_anxiety = models.BooleanField(default=True)
    q6_sleep = models.BooleanField(default=True)
    q7_appetite = models.BooleanField(default=True)
    q8_mood = models.IntegerField()

    def __str__(self):
        return "Quiz Response for " + str(self.elderly) + " from " + self.date.strftime("%Y-%m-%d %H:%M:%S")
