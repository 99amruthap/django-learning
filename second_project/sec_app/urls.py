from django.urls import path, include
from . import views


app_name = 'sec_app'
urlpatterns = [
    path(r"", views.index, name='index'),
    path(r"other/", views.other, name='other'),
    path(r"relative/", views.relative, name='relative'),
    path(r"other/registeration", views.registeration, name='registration'),
    path(r"other/user_login", views.user_login, name='user_login'),
    path(r"other/user_logout", views.user_logout, name='user_logout'),
    path(r"other/special", views.special, name='special'),
]
