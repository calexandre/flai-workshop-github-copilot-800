from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime, timedelta
from pymongo import MongoClient


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting database population...'))
        
        # Clear existing data
        self.stdout.write('Clearing existing data...')
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        
        # Create teams
        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            name='Team Marvel',
            captain_id='',  # Will be set after creating users
            members=[]
        )
        
        team_dc = Team.objects.create(
            name='Team DC',
            captain_id='',
            members=[]
        )
        
        # Create users
        self.stdout.write('Creating users...')
        
        # Marvel superheroes
        iron_man = User.objects.create(
            username='ironman',
            email='ironman@marvel.com',
            first_name='Tony',
            last_name='Stark',
            age=45,
            weight=85.5,
            height=185,
            team_id=str(team_marvel._id)
        )
        
        captain_america = User.objects.create(
            username='captainamerica',
            email='captainamerica@marvel.com',
            first_name='Steve',
            last_name='Rogers',
            age=105,
            weight=90.0,
            height=188,
            team_id=str(team_marvel._id)
        )
        
        black_widow = User.objects.create(
            username='blackwidow',
            email='blackwidow@marvel.com',
            first_name='Natasha',
            last_name='Romanoff',
            age=35,
            weight=59.0,
            height=170,
            team_id=str(team_marvel._id)
        )
        
        thor = User.objects.create(
            username='thor',
            email='thor@marvel.com',
            first_name='Thor',
            last_name='Odinson',
            age=1500,
            weight=290.0,
            height=198,
            team_id=str(team_marvel._id)
        )
        
        hulk = User.objects.create(
            username='hulk',
            email='hulk@marvel.com',
            first_name='Bruce',
            last_name='Banner',
            age=49,
            weight=128.0,
            height=175,
            team_id=str(team_marvel._id)
        )
        
        # DC superheroes
        batman = User.objects.create(
            username='batman',
            email='batman@dc.com',
            first_name='Bruce',
            last_name='Wayne',
            age=42,
            weight=95.0,
            height=188,
            team_id=str(team_dc._id)
        )
        
        superman = User.objects.create(
            username='superman',
            email='superman@dc.com',
            first_name='Clark',
            last_name='Kent',
            age=35,
            weight=107.0,
            height=191,
            team_id=str(team_dc._id)
        )
        
        wonder_woman = User.objects.create(
            username='wonderwoman',
            email='wonderwoman@dc.com',
            first_name='Diana',
            last_name='Prince',
            age=5000,
            weight=75.0,
            height=183,
            team_id=str(team_dc._id)
        )
        
        flash = User.objects.create(
            username='flash',
            email='flash@dc.com',
            first_name='Barry',
            last_name='Allen',
            age=29,
            weight=79.0,
            height=183,
            team_id=str(team_dc._id)
        )
        
        aquaman = User.objects.create(
            username='aquaman',
            email='aquaman@dc.com',
            first_name='Arthur',
            last_name='Curry',
            age=38,
            weight=100.0,
            height=193,
            team_id=str(team_dc._id)
        )
        
        # Update teams with captains and members
        team_marvel.captain_id = str(iron_man._id)
        team_marvel.members = [
            str(iron_man._id),
            str(captain_america._id),
            str(black_widow._id),
            str(thor._id),
            str(hulk._id)
        ]
        team_marvel.save()
        
        team_dc.captain_id = str(batman._id)
        team_dc.members = [
            str(batman._id),
            str(superman._id),
            str(wonder_woman._id),
            str(flash._id),
            str(aquaman._id)
        ]
        team_dc.save()
        
        # Create activities
        self.stdout.write('Creating activities...')
        base_date = datetime.now() - timedelta(days=30)
        
        activities_data = [
            # Marvel activities
            (iron_man, 'Running', 45, 400),
            (iron_man, 'Weight Training', 60, 350),
            (iron_man, 'Cycling', 90, 600),
            (captain_america, 'Running', 60, 550),
            (captain_america, 'Boxing', 45, 420),
            (captain_america, 'Swimming', 50, 480),
            (black_widow, 'Martial Arts', 60, 450),
            (black_widow, 'Yoga', 45, 200),
            (black_widow, 'Running', 40, 380),
            (thor, 'Weight Training', 90, 700),
            (thor, 'Combat Training', 60, 550),
            (hulk, 'Weight Training', 120, 900),
            (hulk, 'Running', 30, 350),
            
            # DC activities
            (batman, 'Martial Arts', 90, 650),
            (batman, 'Weight Training', 60, 450),
            (batman, 'Running', 50, 480),
            (superman, 'Flying', 120, 800),
            (superman, 'Weight Training', 90, 700),
            (wonder_woman, 'Combat Training', 75, 600),
            (wonder_woman, 'Sword Training', 60, 500),
            (flash, 'Running', 180, 1200),
            (flash, 'Cardio', 90, 700),
            (aquaman, 'Swimming', 120, 850),
            (aquaman, 'Weight Training', 60, 450),
        ]
        
        for i, (user, activity_type, duration, calories) in enumerate(activities_data):
            Activity.objects.create(
                user_id=str(user._id),
                activity_type=activity_type,
                duration=duration,
                calories_burned=calories,
                date=base_date + timedelta(days=i % 30),
                notes=f'{activity_type} session for {user.first_name} {user.last_name}'
            )
        
        # Create leaderboard entries
        self.stdout.write('Creating leaderboard...')
        
        users = [
            (iron_man, team_marvel, 1350),
            (captain_america, team_marvel, 1450),
            (black_widow, team_marvel, 1030),
            (thor, team_marvel, 1250),
            (hulk, team_marvel, 1250),
            (batman, team_dc, 1580),
            (superman, team_dc, 1500),
            (wonder_woman, team_dc, 1100),
            (flash, team_dc, 1900),
            (aquaman, team_dc, 1300),
        ]
        
        # Sort by calories to assign ranks
        users_sorted = sorted(users, key=lambda x: x[2], reverse=True)
        
        for rank, (user, team, calories) in enumerate(users_sorted, 1):
            activity_count = Activity.objects.filter(user_id=str(user._id)).count()
            Leaderboard.objects.create(
                user_id=str(user._id),
                user_name=f'{user.first_name} {user.last_name}',
                team_id=str(team._id),
                team_name=team.name,
                total_calories=calories,
                total_activities=activity_count,
                rank=rank
            )
        
        # Create workouts
        self.stdout.write('Creating workout suggestions...')
        
        workouts = [
            {
                'name': 'Super Soldier Strength',
                'activity_type': 'Weight Training',
                'difficulty': 'Advanced',
                'duration': 60,
                'calories_per_session': 450,
                'description': 'Intense strength training inspired by Captain America\'s regimen'
            },
            {
                'name': 'Speedster Sprint',
                'activity_type': 'Running',
                'difficulty': 'Intermediate',
                'duration': 45,
                'calories_per_session': 400,
                'description': 'High-intensity interval running workout'
            },
            {
                'name': 'Amazonian Warrior',
                'activity_type': 'Combat Training',
                'difficulty': 'Advanced',
                'duration': 75,
                'calories_per_session': 600,
                'description': 'Combat and martial arts training routine'
            },
            {
                'name': 'Web-Slinger Cardio',
                'activity_type': 'Cardio',
                'difficulty': 'Beginner',
                'duration': 30,
                'calories_per_session': 250,
                'description': 'Fun cardio workout for beginners'
            },
            {
                'name': 'Atlantean Swim',
                'activity_type': 'Swimming',
                'difficulty': 'Intermediate',
                'duration': 60,
                'calories_per_session': 500,
                'description': 'Full-body swimming workout'
            },
            {
                'name': 'Iron Endurance',
                'activity_type': 'Cycling',
                'difficulty': 'Intermediate',
                'duration': 90,
                'calories_per_session': 600,
                'description': 'Long-distance cycling for stamina building'
            },
            {
                'name': 'Zen Master Yoga',
                'activity_type': 'Yoga',
                'difficulty': 'Beginner',
                'duration': 45,
                'calories_per_session': 200,
                'description': 'Mindful yoga for flexibility and balance'
            },
            {
                'name': 'Dark Knight Boxing',
                'activity_type': 'Boxing',
                'difficulty': 'Advanced',
                'duration': 60,
                'calories_per_session': 550,
                'description': 'Intense boxing workout for combat readiness'
            },
        ]
        
        for workout_data in workouts:
            Workout.objects.create(**workout_data)
        
        # Create unique index on email field using MongoDB directly
        self.stdout.write('Creating unique index on email field...')
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        db.users.create_index([('email', 1)], unique=True)
        
        self.stdout.write(self.style.SUCCESS('Database population completed successfully!'))
        self.stdout.write(self.style.SUCCESS(f'Created {User.objects.count()} users'))
        self.stdout.write(self.style.SUCCESS(f'Created {Team.objects.count()} teams'))
        self.stdout.write(self.style.SUCCESS(f'Created {Activity.objects.count()} activities'))
        self.stdout.write(self.style.SUCCESS(f'Created {Leaderboard.objects.count()} leaderboard entries'))
        self.stdout.write(self.style.SUCCESS(f'Created {Workout.objects.count()} workouts'))
