from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout


class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    team_name = serializers.SerializerMethodField()
    total_points = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'email', 'password', 'team_id', 'team_name', 'total_points', 'created_at']
        extra_kwargs = {'password': {'write_only': True}}
    
    def get_team_name(self, obj):
        if obj.team_id:
            try:
                team = Team.objects.get(id=obj.team_id)
                return team.name
            except Team.DoesNotExist:
                return None
        return None
    
    def get_total_points(self, obj):
        try:
            leaderboard = Leaderboard.objects.get(user_id=str(obj.id))
            return leaderboard.total_calories
        except Leaderboard.DoesNotExist:
            return 0


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'created_at']


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    
    class Meta:
        model = Activity
        fields = ['id', 'user_id', 'activity_type', 'duration', 'calories_burned', 'date', 'notes']


class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    user_name = serializers.SerializerMethodField()
    team_name = serializers.SerializerMethodField()
    points = serializers.IntegerField(source='total_calories', read_only=True)
    
    class Meta:
        model = Leaderboard
        fields = ['id', 'user_id', 'team_id', 'user_name', 'team_name', 'points', 'total_calories', 'total_activities', 'rank', 'updated_at']
    
    def get_user_name(self, obj):
        try:
            user = User.objects.get(id=obj.user_id)
            return user.username or user.name
        except User.DoesNotExist:
            return 'Unknown'
    
    def get_team_name(self, obj):
        if obj.team_id:
            try:
                team = Team.objects.get(id=obj.team_id)
                return team.name
            except Team.DoesNotExist:
                return None
        return None


class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'difficulty', 'duration', 'calories_estimate', 'exercise_list']
