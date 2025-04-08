from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(id="1", name="Test User", email="test@example.com")
        self.assertEqual(user.name, "Test User")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(id="1", name="Test Team", members=["1", "2"])
        self.assertEqual(team.name, "Test Team")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(id="1", user_id="1", type="Running", duration=30, date="2025-04-08")
        self.assertEqual(activity.type, "Running")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard_entry(self):
        entry = Leaderboard.objects.create(id="1", user_id="1", score=100)
        self.assertEqual(entry.score, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(id="1", name="Test Workout", description="A test workout")
        self.assertEqual(workout.name, "Test Workout")
