from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()

class TeamSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)
    members = serializers.ListField(child=serializers.CharField(max_length=100))

class ActivitySerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    user_id = serializers.CharField(max_length=100)
    type = serializers.CharField(max_length=100)
    duration = serializers.IntegerField()
    date = serializers.DateField()

class LeaderboardSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    user_id = serializers.CharField(max_length=100)
    score = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=255)
