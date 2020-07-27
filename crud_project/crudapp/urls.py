from django.urls import path, re_path
from crudapp import views

urlpatterns = [
    re_path(r'^home/$', views.home, name='index'),
    re_path(r'^create/$', views.create, name='create'),
    re_path(r'^update/(?P<id>\d+)/$', views.update, name='update'),
    re_path(r'delete/(?P<id>\d+)/$', views.delete, name='delete'),
]
