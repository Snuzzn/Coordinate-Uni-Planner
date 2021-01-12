from django.urls import path

from . import views

app_name = 'coursePlanner'
urlpatterns = [
    path('all/', views.courses, name='courses'),
    path('new/', views.newCourse, name='newCourse'),
    path('<int:course_id>/', views.course, name='course'),
    path('<int:course_id>/new-contact/', views.newContact, name='newContact'),
]