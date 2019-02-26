from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response

from server.models import (Activity, ActivityType, Caretaker, Comment, Elderly,
                           FamilyMember, QuizResponse)
from server.serializers import (ActivitySerializer, ActivityTypeSerializer,
                                CaretakerSerializer, CommentSerializer,
                                ElderlySerializer, FamilyMemberSerializer,
                                QuizResponseSerializer, UserSerializer)


class UserViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows users to be viewed or edited. """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class CaretakerViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows Caretakers to be viewed or edited. """
    queryset = Caretaker.objects.all()
    serializer_class = CaretakerSerializer


class ElderlyViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows Elderlies to be viewed or edited. """
    queryset = Elderly.objects.all()
    serializer_class = ElderlySerializer


class FamilyMemberViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows Family Members to be viewed or edited. """
    queryset = FamilyMember.objects.all()
    serializer_class = FamilyMemberSerializer


class ActivityTypeViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows FamilyMembers to be viewed or edited. """
    queryset = ActivityType.objects.all()
    serializer_class = ActivityTypeSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows FamilyMembers to be viewed or edited. """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class CommentViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows Comments to be viewed or edited. """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class QuizResponseViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows QuizResponses to be viewed or edited. """
    queryset = QuizResponse.objects.all()
    serializer_class = QuizResponseSerializer
