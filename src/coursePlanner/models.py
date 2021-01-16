from typing import Optional
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    courseCode = models.CharField(max_length=20)
    courseName = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # Return a string representation of the model
        return self.courseCode

class Contact(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    role = models.CharField(max_length=300)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=320)
    location = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Link(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    link = models.CharField(max_length=1000)
    title = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class Query(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'queries'

    def __str__(self):
        return f"{self.text[:50]}..."

class Assessment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    task = models.CharField(max_length=100)
    weighting = models.IntegerField()
    myGrade = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.task 