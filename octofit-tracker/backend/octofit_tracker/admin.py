from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'age', 'team_id', 'created_at')
    list_filter = ('created_at', 'team_id')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    readonly_fields = ('created_at',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'captain_id', 'created_at', 'member_count')
    list_filter = ('created_at',)
    search_fields = ('name', 'captain_id')
    readonly_fields = ('created_at',)
    
    def member_count(self, obj):
        return len(obj.members) if obj.members else 0
    member_count.short_description = 'Members'


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('activity_type', 'user_id', 'duration', 'calories_burned', 'date')
    list_filter = ('activity_type', 'date')
    search_fields = ('user_id', 'activity_type', 'notes')
    date_hierarchy = 'date'


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('rank', 'user_name', 'team_name', 'total_calories', 'total_activities')
    list_filter = ('team_name',)
    search_fields = ('user_name', 'team_name')
    ordering = ('rank',)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'activity_type', 'difficulty', 'duration', 'calories_per_session')
    list_filter = ('activity_type', 'difficulty')
    search_fields = ('name', 'activity_type', 'description')
