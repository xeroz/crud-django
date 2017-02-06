from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.posts_home),
    url(r'^create/', views.post_create),
    url(r'^index/', views.post_list),
]