from django.test import TestCase
from django.utils import timezone
from .models import User, Team, Activity, Leaderboard, Workout


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            name="John Doe",
            email="john@example.com",
            team_id="123"
        )
    
    def test_user_creation(self):
        self.assertEqual(self.user.name, "John Doe")
        self.assertEqual(self.user.email, "john@example.com")
        self.assertEqual(self.user.team_id, "123")
        self.assertIsNotNone(self.user.created_at)
    
    def test_user_str(self):
        self.assertEqual(str(self.user), "John Doe")


class TeamModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(
            name="Team Alpha",
            captain_id="user123",
            members=["user123", "user456"]
        )
    
    def test_team_creation(self):
        self.assertEqual(self.team.name, "Team Alpha")
        self.assertEqual(self.team.captain_id, "user123")
        self.assertEqual(len(self.team.members), 2)
        self.assertIsNotNone(self.team.created_at)
    
    def test_team_str(self):
        self.assertEqual(str(self.team), "Team Alpha")


class ActivityModelTest(TestCase):
    def setUp(self):
        self.activity = Activity.objects.create(
            user_id="user123",
            activity_type="Running",
            duration=30,
            calories_burned=300,
            date=timezone.now(),
            notes="Morning run"
        )
    
    def test_activity_creation(self):
        self.assertEqual(self.activity.user_id, "user123")
        self.assertEqual(self.activity.activity_type, "Running")
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.calories_burned, 300)
        self.assertEqual(self.activity.notes, "Morning run")
    
    def test_activity_str(self):
        self.assertEqual(str(self.activity), "Running - 30 mins")


class LeaderboardModelTest(TestCase):
    def setUp(self):
        self.leaderboard = Leaderboard.objects.create(
            user_id="user123",
            user_name="John Doe",
            team_id="team123",
            team_name="Team Alpha",
            total_calories=1500,
            total_activities=10,
            rank=1
        )
    
    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.user_id, "user123")
        self.assertEqual(self.leaderboard.user_name, "John Doe")
        self.assertEqual(self.leaderboard.team_id, "team123")
        self.assertEqual(self.leaderboard.team_name, "Team Alpha")
        self.assertEqual(self.leaderboard.total_calories, 1500)
        self.assertEqual(self.leaderboard.total_activities, 10)
        self.assertEqual(self.leaderboard.rank, 1)
    
    def test_leaderboard_str(self):
        self.assertEqual(str(self.leaderboard), "John Doe - Rank 1")


class WorkoutModelTest(TestCase):
    def setUp(self):
        self.workout = Workout.objects.create(
            name="HIIT Cardio",
            activity_type="Cardio",
            difficulty="Hard",
            duration=45,
            calories_per_session=500,
            description="High-intensity interval training workout"
        )
    
    def test_workout_creation(self):
        self.assertEqual(self.workout.name, "HIIT Cardio")
        self.assertEqual(self.workout.activity_type, "Cardio")
        self.assertEqual(self.workout.difficulty, "Hard")
        self.assertEqual(self.workout.duration, 45)
        self.assertEqual(self.workout.calories_per_session, 500)
        self.assertIn("High-intensity", self.workout.description)
    
    def test_workout_str(self):
        self.assertEqual(str(self.workout), "HIIT Cardio")
