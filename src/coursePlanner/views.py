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
            return redirect('coordinate:home')
    
    # Display the blank or invalid form
    context = {'form': form}
    template_name = 'coursePlanner/new-course.html'
    return render(request, template_name, context)