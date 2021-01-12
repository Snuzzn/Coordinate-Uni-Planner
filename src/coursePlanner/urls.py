from django.urls import path

from . import views

app_name = 'coursePlanner'
urlpatterns = [
    path('new', views.newCourse, name='newCourse'),
]