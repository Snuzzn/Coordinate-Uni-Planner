from django.urls import path

from . import views

app_name = 'coursePlanner'
urlpatterns = [
    path('all/', views.courses, name='courses'),
    path('new/', views.newCourse, name='newCourse'),
    path('<int:course_id>/', views.course, name='course'),
    path('<int:course_id>/new-contact/', views.newContact, name='newContact'),
    path('<int:course_id>/new-link/', views.newLink, name='newLink'),
    path('<int:course_id>/new-query/', views.newQuery, name='newQuery'),
    path('<int:course_id>/new-assessment/', views.newAssessment, name='newAssessment'),
    path('<int:course_id>/edit-link/<int:link_id>/', views.editLink, name='editLink'),
    path('<int:course_id>/edit-query/<int:query_id>/', views.editQuery, name='editQuery'),
]