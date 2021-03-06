from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.posts_home),
    url(r'^index/', views.post_list, name = 'index'),
    url(r'^create/', views.post_create, name = 'create'),
    url(r'^edit/(?P<id>\w+)/$', views.post_edit, name = 'edit'),
    url(r'^delete/(?P<id>\w+)/$', views.post_delete, name = 'delete'),
]