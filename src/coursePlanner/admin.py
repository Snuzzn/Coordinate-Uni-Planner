from django.contrib import admin

from .models import (
    Course,
    Contact,
    Link,
    Query,
    Assessment,
)
# Register your models here.
admin.site.register(Course)
admin.site.register(Contact)
admin.site.register(Link)
admin.site.register(Query)
admin.site.register(Assessment)

