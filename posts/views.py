from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post

# Create your views here.
def posts_home(request):
    return HttpResponse("<h1>sdfd</h1>")

def post_list(request):
    instance = get_object_or_404(Post, id = 2)
    posts = Post.objects.all()

    context = {
        "posts": posts,
    }

    return render(request, 'post/index.html', context)

def post_create(request):
    
    context = {

    }

    return render(request, 'post/create.html', context)

def post_edit(request, id):
    post = get_object_or_404(Post, id = id)
    
    context = {
        'post': post,
    }

    return render(request, 'post/edit.html', context)

def post_delete(args):
    return HttpResponse("<h1>delete</h1>")