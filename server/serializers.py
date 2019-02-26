from django.contrib.auth.models import User
from rest_framework import serializers

from server.models import (Activity, ActivityType, Caretaker, Comment, Elderly,
                           FamilyMember, QuizResponse)


class UserSerializer(serializers.ModelSerializer):
    """ Serializer for User Model """
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class CaretakerSerializer(serializers.ModelSerializer):
    """ Serializer for Caretaker Model """
    class Meta:
        model = Caretaker
        fields = "__all__"


class ElderlySerializer(serializers.ModelSerializer):
    """ Serializer for Elderly Model """
    class Meta:
        model = Elderly
        fields = "__all__"


class FamilyMemberSerializer(serializers.ModelSerializer):
    """ Serializer for FamilyMember Model """
    class Meta:
        model = FamilyMember
        fields = "__all__"


class ActivityTypeSerializer(serializers.ModelSerializer):
    """ Serializer for ActivityType Model """
    class Meta:
        model = ActivityType
        fields = "__all__"


class ActivitySerializer(serializers.ModelSerializer):
    """ Serializer for Activity Model """
    class Meta:
        model = Activity
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    """ Serializer for Comment Model """
    class Meta:
        model = Comment
        fields = "__all__"


class QuizResponseSerializer(serializers.ModelSerializer):
    """ Serializer for QuizResponse Model """
    class Meta:
        model = QuizResponse
        fields = "__all__"
