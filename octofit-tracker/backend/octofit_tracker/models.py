from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    team_id = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'teams'
    
    def __str__(self):
        return self.name


class Activity(models.Model):
    user_id = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    calories_burned = models.IntegerField()
    date = models.DateTimeField()
    notes = models.TextField(blank=True)
    
    class Meta:
        db_table = 'activities'
        verbose_name_plural = 'activities'
    
    def __str__(self):
        return f"{self.activity_type} - {self.duration} mins"


class Leaderboard(models.Model):
    user_id = models.CharField(max_length=100)
    team_id = models.CharField(max_length=100)
    total_calories = models.IntegerField()
    total_activities = models.IntegerField()
    rank = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'leaderboard'
    
    def __str__(self):
        return f"Rank {self.rank} - {self.user_id}"


class Workout(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    calories_estimate = models.IntegerField()
    exercise_list = models.JSONField()
    
    class Meta:
        db_table = 'workouts'
    
    def __str__(self):
        return self.name
