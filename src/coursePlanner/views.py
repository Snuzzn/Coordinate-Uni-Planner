from django.shortcuts import render, redirect
from .models import (
    Course,
    Contact,
    Link, 
    Query,
    Assessment,
)
from .forms import (
    CourseForm,
    ContactForm,
    LinkForm,
    QueryForm,
    AssessmentForm,
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
    assessments = course.assessment_set.all()
    context = {
        'course': course, 
        'contacts': contacts,
        'links': links,
        'queries': queries,
        'assessments': assessments 
        }
    templateName = 'coursePlanner/course.html'
    return render(request, templateName, context)

def newContact(request, course_id):
    course = Course.objects.get(id=course_id)
    contacts = course.contact_set.all()
    links = course.link_set.all()
    queries = course.query_set.all()
    assessments = course.assessment_set.all()
    
    # Add a new contact
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
        'assessments': assessments, 
        'form': form
        }
    templateName = 'coursePlanner/new-contact.html'
    return render(request, templateName, context)

def newLink(request, course_id):
    course = Course.objects.get(id=course_id)
    contacts = course.contact_set.all()
    links = course.link_set.all()
    queries = course.query_set.all()
    assessments = course.assessment_set.all()
    
    # Add a new contact
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = LinkForm()
    else:
        # POST data submitted; process data.
        form = LinkForm(data=request.POST)
        if form.is_valid():
            newLink = form.save(commit=False)
            newLink.course = course
            newLink.save()
            return redirect('coursePlanner:course', course_id=course_id)
    
    # Display the blank or invalid form
    context = {
        'course': course, 
        'contacts': contacts,
        'links': links,
        'queries': queries,
        'assessments': assessments, 
        'form': form,
        }
    templateName = 'coursePlanner/new-link.html'
    return render(request, templateName, context)

def newQuery(request, course_id):
    course = Course.objects.get(id=course_id)
    contacts = course.contact_set.all()
    links = course.link_set.all()
    queries = course.query_set.all()
    assessments = course.assessment_set.all()
    
    # Add a new contact
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = QueryForm()
    else:
        # POST data submitted; process data.
        form = QueryForm(data=request.POST)
        if form.is_valid():
            newQuery = form.save(commit=False)
            newQuery.course = course
            newQuery.save()
            return redirect('coursePlanner:course', course_id=course_id)
    
    # Display the blank or invalid form
    context = {
        'course': course, 
        'contacts': contacts,
        'links': links,
        'queries': queries,
        'assessments': assessments, 
        'form': form,
        }
    templateName = 'coursePlanner/new-query.html'
    return render(request, templateName, context)

def newAssessment(request, course_id):
    course = Course.objects.get(id=course_id)
    contacts = course.contact_set.all()
    links = course.link_set.all()
    queries = course.query_set.all()
    assessments = course.assessment_set.all()
    
    # Add a new contact
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = AssessmentForm()
    else:
        # POST data submitted; process data.
        form = AssessmentForm(data=request.POST)
        if form.is_valid():
            newAssessment = form.save(commit=False)
            newAssessment.course = course
            newAssessment.save()
            return redirect('coursePlanner:course', course_id=course_id)
    
    # Display the blank or invalid form
    context = {
        'course': course, 
        'contacts': contacts,
        'links': links,
        'queries': queries,
        'assessments': assessments, 
        'form': form,
        }
    templateName = 'coursePlanner/new-assessment.html'
    return render(request, templateName, context)