from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages

from .models import Post
from .forms import PostForm

# Create your views here.


def posts_home(request):
    return HttpResponse("<h1>sdfd</h1>")


def post_list(request):
    posts = Post.objects.all()

    context = {
        "posts": posts,
    }

    return render(request, 'post/index.html', context)


def post_create(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title   = request.POST["title"]
            content = request.POST["content"]

            post = Post(
                title   = title,
                content = content
            )
            post.save()

            return HttpResponseRedirect('/posts/index/')
        else :
            return render(request, 'post/create.html', {'form' : form})
    context = {

    }

    return render(request, 'post/create.html', context)


def post_edit(request, id):

    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        title = request.POST["title"]
        content = request.POST["content"]
        post.title = title
        post.content = content
        post.save()

        return HttpResponseRedirect('/posts/index/')

    context = {
        'post': post,
    }

    return render(request, 'post/edit.html', context)


def post_delete(render, id):

    post = get_object_or_404(Post, id=id)
    post.delete()

    return HttpResponseRedirect('/posts/index/')
