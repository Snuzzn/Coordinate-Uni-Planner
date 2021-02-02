from coursePlanner.models import (
    Course,
    Contact,
    Link, 
    Query,
    Assessment,
)

def createExampleCourse(request):
    course = Course.objects.create(courseCode="PTNS101", courseName="Introduction to Potions", owner=request.user)
    contact1 = Contact.objects.create(course=course, role="Potions Master", name="Horace Slughorn", email="horaceslughorn@hogwarts.com", location="Office 4, Level 6, Hogwarts")
    contact2 = Contact.objects.create(course=course, role="Course Convenor", name="Albus Dumbledore", email="albusdumbledore@hogwarts.com", location="Office 2, Level 2, Hogwarts")
    contact3 = Contact.objects.create(course=course, role="Tutor", name="Tom Riddle", email="tomriddle@hogwarts.com", location="-")
    link1 = Link.objects.create(course=course, link="https://harrypotter.fandom.com/wiki/Potions_(class)", title="Course Outline")
    link2 = Link.objects.create(course=course, link="https://www.hogwartsishere.com/library/book/2884/chapter/1/", title="Magical Drafts and Potions")
    link3 = Link.objects.create(course=course, link="https://www.hogwartsishere.com/library/book/17505/chapter/1/", title="First Year's Guide")
    assessment1 = Assessment.objects.create(course=course, task="Quiz", weighting=10, myGrade=75)
    assessment2 = Assessment.objects.create(course=course, task="Midterm Exam", weighting=20, myGrade=70)
    assessment3 = Assessment.objects.create(course=course, task="Potion Project", weighting=30, myGrade=95)
    assessment4 = Assessment.objects.create(course=course, task="Final", weighting=40)
    query1 = Query.objects.create(course=course, text="What would I get if I added powdered root of asphodel to an infusion of wormwood?")
    query2 = Query.objects.create(course=course, text="What are the side effects of Amortentia?")
    
    course.save()
    contact1.save()
    contact2.save()
    contact3.save()
    link1.save()
    link2.save()
    link3.save()
    assessment1.save()
    assessment2.save()
    assessment3.save()
    assessment4.save()
    query1.save()
    query2.save()
