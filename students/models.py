# -*- coding: utf-8 -*-
from django.db import models
from courses.models import Course

class Student(models.Model):
    name = models.CharField(max_length=70)
    surname = models.CharField(max_length=70)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=75)
    courses = models.ManyToManyField(Course)

    def full_name(self):
        return self.name + ' ' + self.surname

    def __unicode__(self):
        return self.name + ' ' + self.surname
