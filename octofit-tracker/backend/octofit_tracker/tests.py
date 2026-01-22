from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import User, Team, Activity, Leaderboard, Workout
import json


class UserAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'password': 'testpass123'
        }
        self.user = User.objects.create(**self.user_data)
    
    def test_get_users(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_user(self):
        data = {
            'name': 'New User',
            'email': 'newuser@example.com',
            'password': 'newpass123'
        }
        response = self.client.post(reverse('user-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TeamAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.team_data = {
            'name': 'Test Team',
            'description': 'A test team'
        }
        self.team = Team.objects.create(**self.team_data)
    
    def test_get_teams(self):
        response = self.client.get(reverse('team-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_team(self):
        data = {
            'name': 'New Team',
            'description': 'A new team'
        }
        response = self.client.post(reverse('team-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ActivityAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            name='Test User',
            email='test@example.com',
            password='testpass123'
        )
        self.activity_data = {
            'user_id': str(self.user.id),
            'activity_type': 'Running',
            'duration': 30,
            'calories_burned': 300,
            'date': '2024-01-01T12:00:00Z'
        }
        self.activity = Activity.objects.create(**self.activity_data)
    
    def test_get_activities(self):
        response = self.client.get(reverse('activity-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_activity(self):
        data = {
            'user_id': str(self.user.id),
            'activity_type': 'Cycling',
            'duration': 45,
            'calories_burned': 450,
            'date': '2024-01-02T12:00:00Z'
        }
        response = self.client.post(reverse('activity-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LeaderboardAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.leaderboard_data = {
            'user_id': '1',
            'team_id': '1',
            'total_calories': 1000,
            'total_activities': 10,
            'rank': 1
        }
        self.leaderboard = Leaderboard.objects.create(**self.leaderboard_data)
    
    def test_get_leaderboard(self):
        response = self.client.get(reverse('leaderboard-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WorkoutAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.workout_data = {
            'name': 'Test Workout',
            'description': 'A test workout',
            'difficulty': 'medium',
            'duration': 30,
            'calories_estimate': 300,
            'exercise_list': ['pushups', 'squats', 'lunges']
        }
        self.workout = Workout.objects.create(**self.workout_data)
    
    def test_get_workouts(self):
        response = self.client.get(reverse('workout-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_workout(self):
        data = {
            'name': 'New Workout',
            'description': 'A new workout',
            'difficulty': 'hard',
            'duration': 45,
            'calories_estimate': 500,
            'exercise_list': ['burpees', 'mountain climbers']
        }
        response = self.client.post(reverse('workout-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class APIRootTestCase(APITestCase):
    def test_api_root(self):
        response = self.client.get(reverse('api-root'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)
