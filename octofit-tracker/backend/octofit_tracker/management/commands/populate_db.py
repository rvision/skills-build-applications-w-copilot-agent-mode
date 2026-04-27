
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')

        # Users
        users = [
            User(name='Iron Man', email='ironman@marvel.com', team=marvel.name),
            User(name='Captain America', email='cap@marvel.com', team=marvel.name),
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel.name),
            User(name='Batman', email='batman@dc.com', team=dc.name),
            User(name='Superman', email='superman@dc.com', team=dc.name),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc.name),
        ]
        User.objects.bulk_create(users)

        # Activities
        activities = [
            Activity(user='Iron Man', activity='Running', duration=30),
            Activity(user='Captain America', activity='Cycling', duration=45),
            Activity(user='Spider-Man', activity='Swimming', duration=25),
            Activity(user='Batman', activity='Running', duration=40),
            Activity(user='Superman', activity='Cycling', duration=60),
            Activity(user='Wonder Woman', activity='Swimming', duration=35),
        ]
        Activity.objects.bulk_create(activities)

        # Leaderboard
        leaderboard = [
            Leaderboard(team=marvel.name, points=100),
            Leaderboard(team=dc.name, points=90),
        ]
        Leaderboard.objects.bulk_create(leaderboard)

        # Workouts
        workouts = [
            Workout(user='Iron Man', workout='Pushups', reps=50),
            Workout(user='Batman', workout='Situps', reps=60),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data (Django ORM).'))
