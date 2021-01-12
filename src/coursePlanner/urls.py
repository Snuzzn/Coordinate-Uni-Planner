from django.urls import path

from . import views

app_name = 'coursePlanner'
urlpatterns = [
    path('all', views.courses, name='courses'),
    path('new', views.newCourse, name='newCourse'),
]