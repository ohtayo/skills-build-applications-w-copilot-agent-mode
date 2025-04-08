from djongo import models

class User(models.Model):
    _id = models.CharField(max_length=100, primary_key=True)
    id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Team(models.Model):
    _id = models.CharField(max_length=100, primary_key=True)
    id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    members = models.JSONField()

class Activity(models.Model):
    _id = models.CharField(max_length=100, primary_key=True)
    id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()
    date = models.DateField()

class Leaderboard(models.Model):
    _id = models.CharField(max_length=100, primary_key=True)
    id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    score = models.IntegerField()

class Workout(models.Model):
    _id = models.CharField(max_length=100, primary_key=True)
    id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()
