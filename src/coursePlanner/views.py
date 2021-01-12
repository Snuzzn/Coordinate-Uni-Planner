from django.shortcuts import render, redirect
from .models import (
    Course,
    Contact,
    Link, 
    Query,
)
from .forms import (
    CourseForm
)

def courses(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    templateName = 'coursePlanner/courses.html'
    return render(request, templateName, context)


# Create your views here.
def newCourse(request):
    # Add a new course
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = CourseForm()
    else:
        # POST data submitted; process data.
        form = CourseForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('coursePlanner:courses')
    
    # Display the blank or invalid form
    context = {'form': form}
    templateName = 'coursePlanner/new-course.html'
    return render(request, templateName, context)