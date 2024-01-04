from django.contrib import admin
from foreignkeyapp.models import Course,Student

admin.site.register(Course)
admin.site.register(Student)
# Register your models here.