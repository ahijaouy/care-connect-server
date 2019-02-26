from django.db import models
from django.contrib.auth.models import User


class Caretaker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=100, blank=False)


class Elderly(models.Model):
    name = models.TextField(max_length=100, blank=False)
    birth_date = models.DateField()


class FamilyMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=100, blank=False)
    elderly = models.OneToOneField(Elderly, on_delete=models.CASCADE)


class ActivityType(models.Model):
    name = models.TextField(max_length=80, blank=False)
    description = models.TextField(max_length=250, blank=False)
    img_url = models.TextField(blank=True)


class Activity(models.Model):
    activityType = models.OneToOneField(ActivityType, on_delete=models.CASCADE)
    elderly = models.OneToOneField(Elderly, on_delete=models.CASCADE)
    caretaker = models.OneToOneField(Caretaker, on_delete=models.CASCADE)
    duration = models.DurationField()
    date = models.DateField()


class Comment(models.Model):
    elderly = models.OneToOneField(Elderly, on_delete=models.CASCADE)
    caretaker = models.OneToOneField(Caretaker, on_delete=models.CASCADE)
    note = models.TextField(max_length=250, blank=False)
    date = models.DateField()


class QuizResponse(models.Model):
    elderly = models.OneToOneField(Elderly, on_delete=models.CASCADE)
    caretaker = models.OneToOneField(Caretaker, on_delete=models.CASCADE)
    q1 = models.TextField(max_length=250, blank=False)
    q2 = models.TextField(max_length=250, blank=False)
    q3 = models.TextField(max_length=250, blank=False)
    q4 = models.TextField(max_length=250, blank=False)
