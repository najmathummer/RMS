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
    batch = models.CharField(max_length=5, blank=True)
    objects = UserManager()

    

class Semester(models.Model):
	sem = models.CharField(max_length=50)
	#year = models.CharField(max_length=50)
	def __str__(self):
				 return self.sem
class Batch(models.Model):
	div = models.CharField(max_length=1)
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


#events tables

class Section(models.Model):
	sec_name = models.CharField(max_length=50)
	head = models.ForeignKey('auth.User')
	def __str__(self):
				 return self.sec_name
class Classroom(models.Model):
	roomno = models.CharField(max_length=50)
	head = models.ForeignKey('auth.User')

	def __str__(self):
				 return str(self.roomno)			 

class Auditoriums(models.Model):
	audi = models.CharField(max_length=50)
	head = models.ForeignKey('auth.User')

	def __str__(self):
				 return self.audi

class Labs(models.Model):
	name = models.CharField(max_length=50) 
	sec = models.ForeignKey(Section)
	
	def __str__(self):
				 return self.name 

class Graphicshalls(models.Model):
	graph = models.CharField(max_length=50)
	head = models.ForeignKey('auth.User')
	def __str__(self):
				 return self.graph

class Mikesystems(models.Model):
	mike = models.CharField(max_length=50)
	head = models.ForeignKey('auth.User')
	def __str__(self):
				 return self.mike

class Projectors(models.Model):
	pro = models.CharField(max_length=50)
	sec = models.ForeignKey(Section)
	
	
	def __str__(self):
				 return self.pro 

	
class Extension_cables(models.Model):
	cable = models.CharField(max_length=50)
	sec = models.ForeignKey(Section)
	def __str__(self):
				 return self.cable
		       

class Eventprojector(models.Model):
	projector = models.ForeignKey(Projectors)
	date = models.DateField(blank=True, null=True)
	start = models.CharField(max_length=50, null=True)
	end = models.CharField(max_length=50, null=True)
	is_accept = models.IntegerField(default=0)

	def get_absolute_url(self):
		return reverse( 'retest:eventprojectorform')
	def __str__(self):
				 return str(self.id)


class Eventlab(models.Model):
	lab = models.ForeignKey(Labs)
	date = models.DateField(blank=True, null=True)
	start = models.CharField(max_length=50, null=True)
	end = models.CharField(max_length=50, null=True)
	is_accept = models.IntegerField(default=0)

	def get_absolute_url(self):
		return reverse( 'retest:eventlabform')
	def __str__(self):
				 return str(self.id)

class Eventextensioncable(models.Model):
	extension_cable = models.ForeignKey(Extension_cables)
	date = models.DateField(blank=True, null=True)
	start = models.CharField(max_length=50, null=True)
	end = models.CharField(max_length=50, null=True)
	is_accept = models.IntegerField(default=0)	

	def get_absolute_url(self):
		return reverse( 'retest:eventcableform')
	def __str__(self):
				 return str(self.id)


class Eventclassroom(models.Model):
	classroom = models.ForeignKey(Classroom)
	date = models.DateField(blank=True, null=True)
	start = models.CharField(max_length=50, null=True)
	end = models.CharField(max_length=50, null=True)
	is_accept = models.IntegerField(default=0)

	def get_absolute_url(self):
		return reverse( 'retest:eventclassroomform')
	def __str__(self):
				 return str(self.id)


class Eventauditorium(models.Model):
	auditorium = models.ForeignKey(Auditoriums)
	date = models.DateField(blank=True, null=True)
	start = models.CharField(max_length=50, null=True)
	end = models.CharField(max_length=50, null=True)
	is_accept = models.IntegerField(default=0)

	def get_absolute_url(self):
		return reverse( 'retest:eventauditoriumform')
	def __str__(self):
				 return str(self.id)

class Eventmikesystem(models.Model):
	mike_system = models.ForeignKey(Mikesystems)
	date = models.DateField(blank=True, null=True)
	start = models.CharField(max_length=50, null=True)
	end = models.CharField(max_length=50, null=True)
	is_accept = models.IntegerField(default=0)

	def get_absolute_url(self):
		return reverse( 'retest:eventmikesystemform')
	def __str__(self):
				 return str(self.id)	

class Eventgraphicshall(models.Model):
	graphics_hall = models.ForeignKey(Graphicshalls)
	date = models.DateField(blank=True, null=True)
	start = models.CharField(max_length=50, null=True)
	end = models.CharField(max_length=50, null=True)
	is_incharge = models.BooleanField(default=False)
	is_ashok = models.BooleanField(default=False)
	is_principal = models.BooleanField(default=False)

	def get_absolute_url(self):
		return reverse( 'retest:eventgraphicshallform')
	def __str__(self):
				 return str(self.id)			 


