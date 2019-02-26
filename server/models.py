from django.contrib.auth.models import User
from django.db import models


class Caretaker(models.Model):
    """ Model for a Caretaker """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=100, blank=False)

    def __str__(self):
        return self.name


class Elderly(models.Model):
    """ Model for an Elderly """
    name = models.TextField(max_length=100, blank=False)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class FamilyMember(models.Model):
    """ Model for a Family Member """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=100, blank=False)
    elderly = models.OneToOneField(Elderly, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ActivityType(models.Model):
    name = models.TextField(max_length=80, blank=False)
    description = models.TextField(max_length=250, blank=False)
    img_url = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Activity(models.Model):
    activityType = models.OneToOneField(ActivityType, on_delete=models.CASCADE)
    elderly = models.OneToOneField(Elderly, on_delete=models.CASCADE)
    caretaker = models.OneToOneField(Caretaker, on_delete=models.CASCADE)
    duration = models.DurationField()
    date = models.DateTimeField()

    def __str__(self):
        return self.activityType + " on " + self.date

class Comment(models.Model):
    elderly = models.OneToOneField(Elderly, on_delete=models.CASCADE)
    caretaker = models.OneToOneField(Caretaker, on_delete=models.CASCADE)
    note = models.TextField(max_length=250, blank=False)
    date = models.DateTimeField()

    def __str__(self):
        return self.note[:10] + "..."


class QuizResponse(models.Model):
    elderly = models.OneToOneField(Elderly, on_delete=models.CASCADE)
    caretaker = models.OneToOneField(Caretaker, on_delete=models.CASCADE)
    date = models.DateTimeField()
    q1 = models.TextField(max_length=250, blank=False)
    q2 = models.TextField(max_length=250, blank=False)
    q3 = models.TextField(max_length=250, blank=False)
    q4 = models.TextField(max_length=250, blank=False)
