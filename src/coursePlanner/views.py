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
    DeleteContactForm,
    DeleteLinkForm,
    DeleteQueryForm,
    DeleteAssessmentForm,
)

def courses(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    templateName = 'coursePlanner/courses.html'
    return render(request, templateName, context)


# Create your views here.
def newCourse(request):
    # Add a new course

    form = CourseForm(request.POST or None)
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
    
    form = ContactForm(request.POST or None)
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
    
    form = LinkForm(request.POST or None) 
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
    
    form = QueryForm(request.POST or None)
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
    
    # Add a new assessment
    form = AssessmentForm(request.POST or None)
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

def editContact(request, course_id, contact_id):
    """Edit an existing contact."""
    contact = Contact.objects.get(id=contact_id)
    course = Course.objects.get(id=course_id)
    contacts = course.contact_set.all()
    links = course.link_set.all()
    queries = course.query_set.all()
    assessments = course.assessment_set.all()
 
    form = ContactForm(request.POST or None, instance=contact)
    if form.is_valid():
        form.save()
        return redirect('coursePlanner:course', course_id=course_id)

    # Display the blank or invalid form
    context = {
        'course': course, 
        'contacts': contacts,
        'links': links,
        'queries': queries,
        'assessments': assessments, 
        'form': form,
        'contactToEdit': contact,
    }
    templateName = 'coursePlanner/edit-contact.html'
    return render(request, templateName, context)

def editLink(request, course_id, link_id):
    """Edit an existing link."""
    link = Link.objects.get(id=link_id)
    course = Course.objects.get(id=course_id)
    contacts = course.contact_set.all()
    links = course.link_set.all()
    queries = course.query_set.all()
    assessments = course.assessment_set.all()

    form = LinkForm(request.POST or None, instance=link)
    if form.is_valid():
        form.save()
        return redirect('coursePlanner:course', course_id=course_id)

    # Display the blank or invalid form
    context = {
        'course': course, 
        'contacts': contacts,
        'links': links,
        'queries': queries,
        'assessments': assessments, 
        'form': form,
        'linkToEdit': link,
    }
    templateName = 'coursePlanner/edit-link.html'
    return render(request, templateName, context)
    
def editQuery(request, course_id, query_id):
    """Edit an existing query."""
    query = Query.objects.get(id=query_id)
    course = Course.objects.get(id=course_id)
    contacts = course.contact_set.all()
    links = course.link_set.all()
    queries = course.query_set.all()
    assessments = course.assessment_set.all()

 
    form = QueryForm(request.POST or None, instance=query)
    if form.is_valid():
        form.save()
        return redirect('coursePlanner:course', course_id=course_id)

    # Display the blank or invalid form
    context = {
        'course': course, 
        'contacts': contacts,
        'links': links,
        'queries': queries,
        'assessments': assessments, 
        'form': form,
        'queryToEdit': query,
    }
    templateName = 'coursePlanner/edit-query.html'
    return render(request, templateName, context)


def editAssessment(request, course_id, assessment_id):
    """Edit an existing query."""
    assessment = Assessment.objects.get(id=assessment_id)
    course = Course.objects.get(id=course_id)
    contacts = course.contact_set.all()
    links = course.link_set.all()
    queries = course.query_set.all()
    assessments = course.assessment_set.all()

    form = AssessmentForm(request.POST or None, instance=assessment)
    if form.is_valid():
        form.save()
        return redirect('coursePlanner:course', course_id=course_id)

    # Display the blank or invalid form
    context = {
        'course': course, 
        'contacts': contacts,
        'links': links,
        'queries': queries,
        'assessments': assessments, 
        'form': form,
        'assessmentToEdit': assessment,
    }
    templateName = 'coursePlanner/edit-assessment.html'
    return render(request, templateName, context)
    
def deleteContact(request, course_id, contact_id):
    course = Course.objects.get(id=course_id)
    contacts = course.contact_set.all()
    links = course.link_set.all()
    queries = course.query_set.all()
    assessments = course.assessment_set.all()
    contactToDelete = Contact.objects.get(id=contact_id)
    
    form = DeleteContactForm(request.POST or None)
    if form.is_valid():
        contactToDelete.delete()
        return redirect('coursePlanner:course', course_id=course_id)
        
    # Display the blank or invalid form
    context = {
        'course': course, 
        'contacts': contacts,
        'links': links,
        'queries': queries,
        'assessments': assessments, 
        'form': form,
        'contactToDelete': contactToDelete,
    }
    templateName = 'coursePlanner/delete-contact.html'
    return render(request, templateName, context)

def deleteLink(request, course_id, link_id):
    course = Course.objects.get(id=course_id)
    contacts = course.contact_set.all()
    links = course.link_set.all()
    queries = course.query_set.all()
    assessments = course.assessment_set.all()
    linkToDelete = Link.objects.get(id=link_id)
    
    form = DeleteLinkForm(request.POST or None)
    if form.is_valid():
        linkToDelete.delete()
        return redirect('coursePlanner:course', course_id=course_id)
        
    # Display the blank or invalid form
    context = {
        'course': course, 
        'contacts': contacts,
        'links': links,
        'queries': queries,
        'assessments': assessments, 
        'form': form,
        'linkToDelete': linkToDelete,
    }
    templateName = 'coursePlanner/delete-link.html'
    return render(request, templateName, context)

def deleteQuery(request, course_id, query_id):
    course = Course.objects.get(id=course_id)
    contacts = course.contact_set.all()
    links = course.link_set.all()
    queries = course.query_set.all()
    assessments = course.assessment_set.all()
    queryToDelete = Query.objects.get(id=query_id)
    
    form = DeleteQueryForm(request.POST or None)
    if form.is_valid():
        queryToDelete.delete()
        return redirect('coursePlanner:course', course_id=course_id)
        
    # Display the blank or invalid form
    context = {
        'course': course, 
        'contacts': contacts,
        'links': links,
        'queries': queries,
        'assessments': assessments, 
        'form': form,
        'queryToDelete': queryToDelete,
    }
    templateName = 'coursePlanner/delete-query.html'
    return render(request, templateName, context)

def deleteAssessment(request, course_id, assessment_id):
    course = Course.objects.get(id=course_id)
    contacts = course.contact_set.all()
    links = course.link_set.all()
    queries = course.query_set.all()
    assessments = course.assessment_set.all()
    assessmentToDelete = Assessment.objects.get(id=assessment_id)
    
    form = DeleteAssessmentForm(request.POST or None)
    if form.is_valid():
        assessmentToDelete.delete()
        return redirect('coursePlanner:course', course_id=course_id)
        
    # Display the blank or invalid form
    context = {
        'course': course, 
        'contacts': contacts,
        'links': links,
        'queries': queries,
        'assessments': assessments, 
        'form': form,
        'assessmentToDelete': assessmentToDelete,
    }
    templateName = 'coursePlanner/delete-assessment.html'
    return render(request, templateName, context)