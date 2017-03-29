#!/usr/bin/python -tt
from django.db import models
from django.core.urlresolvers import reverse


from django.contrib.auth.models import User, UserManager
from django.db.models.signals import post_save





class Departement(models.Model):
	dept = models.CharField(max_length=50)
	hod = models.ForeignKey('auth.User')
	def __str__(self):
				 return self.dept

class CustomUser(User):
    
    dept = models.ForeignKey(Departement)
    avatar = models.ImageField(upload_to='/', null=True, blank=True)
    batch = models.CharField(max_length=5, blank=True)
    objects = UserManager()

    

class Semester(models.Model):
	sem = models.CharField(max_length=50)
	#year = models.CharField(max_length=50)
	def __str__(self):
				 return self.sem
class Batch(models.Model):
	div = models.CharField(max_length=1)
	#year = models.CharField(max_length=50)
	def __str__(self):
				 return self.div


	
	
	

class Subject(models.Model):
	dept = models.ForeignKey(Departement)
	semester = models.ForeignKey(Semester)
	sub = models.CharField(max_length=50)

	def __str__(self):
				 return self.sub
	
class Student(models.Model):
	name = models.CharField(max_length=50)
	admnno = models.CharField(max_length=50)
	dept = models.ForeignKey(Departement)
	sem = models.ForeignKey(Semester)
	batch = models.ForeignKey(Batch)
	def __str__(self):
				 return self.name + '-' + self.admnno
	
class Retest(models.Model):
	semester = models.ForeignKey(Semester)
	dept = models.ForeignKey(Departement)
	batch = models.ForeignKey(Batch)
	date = models.DateField(blank=True, null=True)
	subject = models.ForeignKey(Subject)
	name = models.CharField(max_length=50)
	admnno = models.CharField(max_length=50)
	reason = models.CharField(max_length=50)
	proof = models.CharField(max_length=200)
	is_hod = models.BooleanField(default=False)
	is_principal = models.BooleanField(default=False)

	def get_absolute_url(self):
		return reverse( 'retest:retestform')
	def __str__(self):
				 return self.name

