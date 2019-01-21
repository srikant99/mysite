from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('posts', views.post_list, name='post_list'),
    path('posts/(?P<pk>[0-9]+)', views.post_detail, name='post_detail'),
    path('posts/(?P<pk>[0-9]+)/comment', views.post_comment, name='post_comment'),
    path('posts/(?P<pk>[0-9]+)/comment/add_comment', views.add_comment, name='add_comment'),

]