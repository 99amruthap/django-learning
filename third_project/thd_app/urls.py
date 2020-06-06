from django.urls import path, re_path
from . import views

app_name = 'thd_app'
urlpatterns = [
    path(r'index/', views.IndexView.as_view(), name='index'),
    path(r'<slug:pk>/', views.SchoolDetailView.as_view(), name='detail'),
    re_path(r'school_list/', views.SchoolListView.as_view(), name='list'),
]
