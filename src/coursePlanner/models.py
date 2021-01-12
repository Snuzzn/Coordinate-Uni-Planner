from django.db import models

# Create your models here.
class Course(models.Model):
    courseCode = models.CharField(max_length=20)
    courseName = models.CharField(max_length=100)

    def __str__(self):
        # Return a string representation of the model
        return self.courseCode

class Contact(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    role = models.CharField(max_length=300)
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
    query = models.TextField()

    class Meta:
        verbose_name_plural = 'queries'

    def __str__(self):
        return f"{self.query[:50]}..."

    
