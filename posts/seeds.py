from .models import Post


class PostTableSeeder():

    def run(self):

        Post.objects.all().delete()

        Post(
            pk = 1,
            title = 'title',
            content = 'content'
        ).save()

        Post(
            pk = 2,
            title   = 'title2',
            content = 'content2'
        ).save()