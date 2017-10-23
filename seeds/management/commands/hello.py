from django.core.management.base import BaseCommand, CommandError
from posts.seeds import PostTableSeeder

class Command(BaseCommand):

    def handle(self, *args, **options):
        test = 'hello'
        PostTableSeeder().run()
        return test
