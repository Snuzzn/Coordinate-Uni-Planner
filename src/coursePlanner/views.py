from django.shortcuts import render, redirect
from .models import (
    Course,
    Contact,
    Link, 
    Query,
)
from .forms import (
    CourseForm,
    ContactForm
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

def course(request, course_id):
    course = Course.objects.get(id=course_id)
    contacts = course.contact_set.all()
    links = course.link_set.all()
    queries = course.query_set.all()
    context = {
        'course': course, 
        'contacts': contacts,
        'links': links,
        'queries': queries }
    templateName = 'coursePlanner/course.html'
    return render(request, templateName, context)

def newContact(request, course_id):
    course = Course.objects.get(id=course_id)
    contacts = course.contact_set.all()
    links = course.link_set.all()
    queries = course.query_set.all()
    # form to add new contact
    
    # Add a new course
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ContactForm()
    else:
        # POST data submitted; process data.
        form = ContactForm(data=request.POST)
        if form.is_valid():
            newContact = form.save(commit=False)
            newContact.course = course
            newContact.save()
            return redirect('coursePlanner:course', course_id=course_id)
    
    # Display the blank or invalid form
    context = {
        'course': course, 
        'contacts': contacts,
        'links': links,
        'queries': queries,
        'form': form
        }
    templateName = 'coursePlanner/new-contact.html'
    return render(request, templateName, context) 