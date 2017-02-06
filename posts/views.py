from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def posts_home(request):
    return HttpResponse("<h1>sdfd</h1>")

def post_list(request):

    context = {
        "title": "Detail",
    }

    return render(request, 'index.html', context)

def post_create(request):
    return HttpResponse("<h1>create</h1>")

def post_update(args):
    return HttpResponse("<h1>edit</h1>")

def post_delete(args):
    return HttpResponse("<h1>delete</h1>")