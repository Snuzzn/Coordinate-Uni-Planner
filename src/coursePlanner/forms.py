from django import forms

from .models import (
    Course,
    Contact,
    Link,
    Query,
)

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['courseCode', 'courseName']
        labels = {
            'courseCode': 'Course Code',
            'courseName': 'Course Name',
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['role', 'name', 'email', 'location']
        labels = {
            'role': 'Role',
            'name': 'Name',
            'email': 'Email',
            'location': 'Location',
        }
