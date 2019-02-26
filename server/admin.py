from django.contrib import admin
from .models import Caretaker, Elderly, FamilyMember, ActivityType, Activity, Comment, QuizResponse

admin.site.register(Caretaker)
admin.site.register(Elderly)
admin.site.register(FamilyMember)
admin.site.register(ActivityType)
admin.site.register(Activity)
admin.site.register(Comment)
admin.site.register(QuizResponse)
