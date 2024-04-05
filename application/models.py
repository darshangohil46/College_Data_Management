from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    enrollment = models.CharField(max_length=500)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name
