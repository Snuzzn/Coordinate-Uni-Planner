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