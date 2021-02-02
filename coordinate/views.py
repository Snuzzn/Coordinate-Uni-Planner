from django.shortcuts import render
from coursePlanner.models import (
    Course
)

def home(request):
    if (request.user.is_authenticated == True):
        courses = Course.objects.filter(owner=request.user)
        context = {'courses': courses}
    else:
        context = {}
    return render(request, "index.html", context)
    # return render(request, "index.html")