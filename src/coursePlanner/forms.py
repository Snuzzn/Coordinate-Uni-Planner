from django import forms

from .models import (
    Assessment, Course,
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

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['link', 'title']
        labels = {
            'link': 'Link',
            'title': 'Title',
        }

class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ['text']
        labels = {
            'text': 'Query'
        }

class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ['task', 'weighting', 'myGrade']
        labels = {
            'task': 'Task',
            'weighting': 'Weighting',
            'myGrade': 'My Grade',
        }