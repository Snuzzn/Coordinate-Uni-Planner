from typing import NewType
from django import forms



from .models import (
    Assessment, 
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
        widgets = {
            'courseCode' : forms.TextInput(attrs = {'placeholder': 'Course Code'}),
            'courseName' : forms.TextInput(attrs = {'placeholder': 'Course Name'}),
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
        widgets = {
            'role' : forms.TextInput(attrs = {'placeholder': 'Role'}),
            'name'    : forms.TextInput(attrs = {'placeholder': 'Name'}),
            'email'    : forms.TextInput(attrs = {'placeholder': 'Email'}),
            'location'    : forms.TextInput(attrs = {'placeholder': 'Location'}),
        }

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['link', 'title']
        labels = {
            'link': 'Link',
            'title': 'Title',
        }
        widgets = {
            'link' : forms.TextInput(attrs = {'placeholder': 'Link'}),
            'title'    : forms.TextInput(attrs = {'placeholder': 'Title'}),
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
        widgets = {
            'task' : forms.TextInput(attrs = {'placeholder': 'Assignment 1'}),
            'weighting'    : forms.TextInput(attrs = {'placeholder': '15%'}),
            'myGrade'    : forms.TextInput(attrs = {'placeholder': '80%'}),
        }

    def clean_myGrade(self):
        grade = self.cleaned_data.get("myGrade")
        if type(grade) is int:
            if grade > 100 or grade < 0:
                raise forms.ValidationError("Grade must be in the range of 0 - 100")
            else:
                return grade

    # def clean_weighting(self):

    #     assessments = Assessment.objects.all()
    #     total = 0
    #     for assessment in assessments:
    #         total += assessment.weighting
        
    #     weighting = self.cleaned_data.get("weighting")

    #     if len(self.initial) != 0: # the form was not blank at first (aka. edit) 
    #         oldWeighting = self.initial['weighting']
    #         if weighting + total - oldWeighting > 100:
    #            raise forms.ValidationError("Total weighting must not exceed 100")
    #         else:
    #             return weighting
        
    #     # the form was blank at first (aka. new)
    #     if (weighting + total) > 100:
    #         raise forms.ValidationError("Total weighting must not exceed 100")
    #     else:
    #         return weighting

class DeleteContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = []

class DeleteLinkForm(forms.ModelForm):
    class Meta:
        model = Link 
        fields = []

class DeleteAssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment 
        fields = []
        
class DeleteQueryForm(forms.ModelForm):
    class Meta:
        model = Query 
        fields = []

class DeleteCourseForm(forms.ModelForm):
    class Meta:
        model = Course 
        fields = []