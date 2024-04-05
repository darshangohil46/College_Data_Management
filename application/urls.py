from django.contrib import admin
from django.urls import path
from application.views import *


urlpatterns = [
    path("", index, name="home"),
    path("about", about, name="about"),
    path("event", event, name="event"),
    path("student", student, name="student"),
    path("faculty", faculty, name="faculty"),
    path("adminfile", adminfile, name="adminfile"),
]
