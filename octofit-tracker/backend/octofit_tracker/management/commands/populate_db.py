from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime, timedelta
import random


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
        
        # Create Teams
        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Avengers assemble! Fighting for fitness and glory!'
        )
        
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League united for ultimate wellness!'
        )
        
        # Create Users (Superheroes)
        self.stdout.write('Creating superhero users...')
        marvel_heroes = [
            {'name': 'Iron Man', 'username': 'ironman', 'email': 'tony.stark@marvel.com', 'password': 'iamironman123'},
            {'name': 'Captain America', 'username': 'captainamerica', 'email': 'steve.rogers@marvel.com', 'password': 'captainamerica123'},
            {'name': 'Thor', 'username': 'thor', 'email': 'thor.odinson@marvel.com', 'password': 'godofthunder123'},
            {'name': 'Black Widow', 'username': 'blackwidow', 'email': 'natasha.romanoff@marvel.com', 'password': 'blackwidow123'},
            {'name': 'Hulk', 'username': 'hulk', 'email': 'bruce.banner@marvel.com', 'password': 'hulksmash123'},
            {'name': 'Spider-Man', 'username': 'spiderman', 'email': 'peter.parker@marvel.com', 'password': 'spiderman123'},
        ]
        
        dc_heroes = [
            {'name': 'Superman', 'username': 'superman', 'email': 'clark.kent@dc.com', 'password': 'manofsteel123'},
            {'name': 'Batman', 'username': 'batman', 'email': 'bruce.wayne@dc.com', 'password': 'darkknight123'},
            {'name': 'Wonder Woman', 'username': 'wonderwoman', 'email': 'diana.prince@dc.com', 'password': 'wonderwoman123'},
            {'name': 'The Flash', 'username': 'theflash', 'email': 'barry.allen@dc.com', 'password': 'theflash123'},
            {'name': 'Aquaman', 'username': 'aquaman', 'email': 'arthur.curry@dc.com', 'password': 'aquaman123'},
            {'name': 'Green Lantern', 'username': 'greenlantern', 'email': 'hal.jordan@dc.com', 'password': 'greenlantern123'},
        ]
        
        marvel_users = []
        for hero in marvel_heroes:
            user = User.objects.create(
                name=hero['name'],
                username=hero['username'],
                email=hero['email'],
                password=hero['password'],
                team_id=str(team_marvel.id)
            )
            marvel_users.append(user)
        
        dc_users = []
        for hero in dc_heroes:
            user = User.objects.create(
                name=hero['name'],
                username=hero['username'],
                email=hero['email'],
                password=hero['password'],
                team_id=str(team_dc.id)
            )
            dc_users.append(user)
        
        all_users = marvel_users + dc_users
        
        # Create Activities
        self.stdout.write('Creating activities...')
        activity_types = ['Running', 'Cycling', 'Swimming', 'Weight Training', 'Yoga', 'Boxing', 'HIIT', 'Pilates']
        
        for user in all_users:
            num_activities = random.randint(5, 15)
            for i in range(num_activities):
                activity_type = random.choice(activity_types)
                duration = random.randint(15, 120)
                calories = duration * random.randint(5, 12)
                days_ago = random.randint(0, 30)
                
                Activity.objects.create(
                    user_id=str(user.id),
                    activity_type=activity_type,
                    duration=duration,
                    calories_burned=calories,
                    date=datetime.now() - timedelta(days=days_ago),
                    notes=f'{user.name} completed {activity_type} session'
                )
        
        # Create Leaderboard entries
        self.stdout.write('Creating leaderboard entries...')
        leaderboard_data = []
        for user in all_users:
            activities = Activity.objects.filter(user_id=str(user.id))
            total_calories = sum(act.calories_burned for act in activities)
            total_activities = activities.count()
            
            leaderboard_data.append({
                'user': user,
                'total_calories': total_calories,
                'total_activities': total_activities
            })
        
        # Sort by total calories
        leaderboard_data.sort(key=lambda x: x['total_calories'], reverse=True)
        
        for rank, entry in enumerate(leaderboard_data, start=1):
            Leaderboard.objects.create(
                user_id=str(entry['user'].id),
                team_id=entry['user'].team_id,
                total_calories=entry['total_calories'],
                total_activities=entry['total_activities'],
                rank=rank
            )
        
        # Create Workouts
        self.stdout.write('Creating workout routines...')
        workouts = [
            {
                'name': 'Thor\'s Hammer Workout',
                'description': 'Build god-like strength with this intense routine',
                'difficulty': 'Hard',
                'duration': 60,
                'calories_estimate': 600,
                'exercise_list': ['Hammer Curls', 'Overhead Press', 'Deadlifts', 'Pull-ups']
            },
            {
                'name': 'Spider-Man Agility Training',
                'description': 'Enhance your agility and flexibility',
                'difficulty': 'Medium',
                'duration': 45,
                'calories_estimate': 400,
                'exercise_list': ['Jump Squats', 'Burpees', 'Mountain Climbers', 'Box Jumps']
            },
            {
                'name': 'Captain America Shield Circuit',
                'description': 'Full-body circuit training for peak performance',
                'difficulty': 'Hard',
                'duration': 50,
                'calories_estimate': 550,
                'exercise_list': ['Push-ups', 'Kettlebell Swings', 'Battle Ropes', 'Plank']
            },
            {
                'name': 'Flash Speed Training',
                'description': 'Build explosive speed and endurance',
                'difficulty': 'Medium',
                'duration': 40,
                'calories_estimate': 500,
                'exercise_list': ['Sprints', 'High Knees', 'Ladder Drills', 'Jump Rope']
            },
            {
                'name': 'Wonder Woman Warrior Workout',
                'description': 'Develop warrior-like strength and grace',
                'difficulty': 'Medium',
                'duration': 45,
                'calories_estimate': 450,
                'exercise_list': ['Lunges', 'Dumbbell Rows', 'Shoulder Press', 'Core Twists']
            },
            {
                'name': 'Hulk Smash Strength',
                'description': 'Maximum strength building routine',
                'difficulty': 'Hard',
                'duration': 70,
                'calories_estimate': 700,
                'exercise_list': ['Squats', 'Bench Press', 'Deadlifts', 'Farmer\'s Walk']
            },
            {
                'name': 'Black Widow Flexibility Flow',
                'description': 'Improve flexibility and core strength',
                'difficulty': 'Easy',
                'duration': 30,
                'calories_estimate': 250,
                'exercise_list': ['Yoga Flow', 'Stretching', 'Pilates', 'Core Work']
            },
            {
                'name': 'Aquaman Swimming Circuit',
                'description': 'Build endurance with water-inspired exercises',
                'difficulty': 'Medium',
                'duration': 45,
                'calories_estimate': 480,
                'exercise_list': ['Swimming', 'Water Aerobics', 'Resistance Training', 'Cool Down']
            },
        ]
        
        for workout_data in workouts:
            Workout.objects.create(**workout_data)
        
        self.stdout.write(self.style.SUCCESS('Database population completed successfully!'))
        self.stdout.write(self.style.SUCCESS(f'Created {Team.objects.count()} teams'))
        self.stdout.write(self.style.SUCCESS(f'Created {User.objects.count()} users'))
        self.stdout.write(self.style.SUCCESS(f'Created {Activity.objects.count()} activities'))
        self.stdout.write(self.style.SUCCESS(f'Created {Leaderboard.objects.count()} leaderboard entries'))
        self.stdout.write(self.style.SUCCESS(f'Created {Workout.objects.count()} workouts'))
