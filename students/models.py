from django.db import models
from courses.models import Course

class Student(models.Model):
    name = models.CharField(max_length = 255)
    surname = models.CharField(max_length = 255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length = 25, null = True, blank = True)
    address = models.CharField(max_length = 255, null = True, blank = True)
    skype = models.CharField(max_length = 255)
    courses = models.ManyToManyField(Course)

    def full_name(self):
        return self.name + " " + self.surname

    def __unicode__(self):
        return self.name + " " + self.surname