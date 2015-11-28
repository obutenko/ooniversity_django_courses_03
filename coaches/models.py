from django.db import models
from django.contrib.auth.models import User, AnonymousUser

class Coach(models.Model):
	user = models.OneToOneField(User)
	date_of_birth = models.DateField()
	gender = models.CharField(max_length = 10, choices=(('M', 'Male'),('F', 'Femail')))
	phone = models.CharField(max_length = 25, null = True, blank = True)
	address = models.CharField(max_length = 255, null = True, blank = True)
	skype = models.CharField(max_length = 255)
	description = models.TextField()
	
	def name(self):
		return self.user.first_name
	def surname(self):
		return self.user.last_name
	def __unicode__(self):
		return self.user.first_name
