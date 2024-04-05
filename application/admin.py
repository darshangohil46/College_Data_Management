from django.contrib import admin

# Register your models here.
from application.models import Student
from application.models import Faculty

admin.site.register(Student)
admin.site.register(Faculty)
