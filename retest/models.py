#!/usr/bin/python -tt
from django.db import models
from django.core.urlresolvers import reverse


from django.contrib.auth.models import User, UserManager, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver





class Departement(models.Model):
	dept = models.CharField(max_length=50)
	hod = models.ForeignKey('auth.User')
	def __str__(self):
				 return self.dept



class HeadofDept(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dept = models.ForeignKey(Departement, default=0)
    def __str__(self):
				 return str(self.user)
class Batch(models.Model):
	div = models.CharField(max_length=1)
	def __str__(self):
				 return self.div
class Semester(models.Model):
	sem = models.CharField(max_length=50)
	#year = models.CharField(max_length=50)
	def __str__(self):
				 return self.sem

class Rep(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dept = models.ForeignKey(Departement, default=0)
    batch = models.ForeignKey(Batch, default=0)
    semester = models.ForeignKey(Semester, default=0)
    
    def __str__(self):
				 return str(self.user)
class allusers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='retest/static/images/')
    def __str__(self):
				 return str(self.user)




    





class Subject(models.Model):
	dept = models.ForeignKey(Departement)
	semester = models.ForeignKey(Semester)
	sub = models.CharField(max_length=50)

	def __str__(self):
				 return self.sub
	

	
class Retest(models.Model):
	
	semester = models.ForeignKey(Semester)
	dept = models.ForeignKey(Departement)
	batch = models.ForeignKey(Batch)
	date = models.DateField(default=0)
	subject = models.ForeignKey(Subject)
	name = models.CharField(max_length=50)
	admnno = models.CharField(max_length=50)
	reason = models.CharField(max_length=50)
	proof = models.CharField(max_length=200)
	is_hod = models.BooleanField(default=False)
	is_principal = models.BooleanField(default=False)
	notify = models.BooleanField(default=False)
	is_sure = models.BooleanField(default=False)
	

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
	available = models.BooleanField(default=True)
	
	def __str__(self):
				 return str(self.roomno)			 

class Auditoriums(models.Model):
	audi = models.CharField(max_length=50)
	sec = models.ForeignKey(Section, default=0)
	available = models.BooleanField(default=True)

	def __str__(self):
				 return self.audi

class Labs(models.Model):
	name = models.CharField(max_length=50) 
	sec = models.ForeignKey(Section, default=0)
	available = models.BooleanField(default=True)
	
	def __str__(self):
				 return self.name + '-' +  str(self.sec)  

class Graphicshalls(models.Model):
	graph = models.CharField(max_length=50)
	sec = models.ForeignKey(Section, default=0)
	available = models.BooleanField(default=True)
	def __str__(self):
				 return self.graph

class Mikesystems(models.Model):
	mike = models.CharField(max_length=50)
	sec = models.ForeignKey(Section, default=0)
	available = models.BooleanField(default=True)
	def __str__(self):
				 return self.mike + '-' +  str(self.sec)

class Projectors(models.Model):
	pro = models.CharField(max_length=50)
	sec = models.ForeignKey(Section, default=0)
	available = models.BooleanField(default=True)
	
	
	def __str__(self):
				 return self.pro + '-' +  str(self.sec) 

	
class Extension_cables(models.Model):
	cable = models.CharField(max_length=50)
	sec = models.ForeignKey(Section, default=0)
	available = models.BooleanField(default=True)
	def __str__(self):
				 return self.cable  + '-' + str(self.sec) 
		       

class Eventprojector(models.Model):
	projector = models.ForeignKey(Projectors, limit_choices_to={'available': True},)
	date = models.DateField(blank=True, null=True)
	start = models.CharField(max_length=50, null=True)
	end = models.CharField(max_length=50, null=True)
	is_accept = models.BooleanField(default=False)
	is_incharge = models.BooleanField(default=False)
	is_head = models.BooleanField(default=False) 
	recieved = models.BooleanField(default=False) 
	def get_absolute_url(self):
		return reverse( 'retest:eventprojectorform')
	def __str__(self):
				 return str(self.id)


class Eventlab(models.Model):
	lab = models.ForeignKey(Labs, limit_choices_to={'available': True},)
	date = models.DateField(blank=True, null=True)
	start = models.CharField(max_length=50, null=True)
	end = models.CharField(max_length=50, null=True)
	is_accept = models.BooleanField(default=False)
	is_incharge = models.BooleanField(default=False)
	is_head = models.BooleanField(default=False) 
	recieved = models.BooleanField(default=False) 

	def get_absolute_url(self):
		return reverse( 'retest:eventlabform')
	def __str__(self):
				 return str(self.id)

class Eventextensioncable(models.Model):
	extension_cable = models.ForeignKey(Extension_cables, limit_choices_to={'available': True},)
	date = models.DateField(blank=True, null=True)
	start = models.CharField(max_length=50, null=True)
	end = models.CharField(max_length=50, null=True)
	is_accept = models.BooleanField(default=False)
	is_incharge = models.BooleanField(default=False)
	is_head = models.BooleanField(default=False) 
	recieved = models.BooleanField(default=False) 
	def get_absolute_url(self):
		return reverse( 'retest:eventextensioncableform')
	def __str__(self):
				 return str(self.id)


class Eventclassroom(models.Model):
	classroom = models.ForeignKey(Classroom, limit_choices_to={'available': True},)
	date = models.DateField(blank=True, null=True)
	start = models.CharField(max_length=50, null=True)
	end = models.CharField(max_length=50, null=True)
	is_accept = models.BooleanField(default=False)
	is_incharge = models.BooleanField(default=False)
	recieved = models.BooleanField(default=False) 
	

	def get_absolute_url(self):
		return reverse( 'retest:eventclassroomform')
	def __str__(self):
				 return str(self.id)


class Eventauditorium(models.Model):
	auditorium = models.ForeignKey(Auditoriums, limit_choices_to={'available': True},)
	date = models.DateField(blank=True, null=True)
	start = models.CharField(max_length=50, null=True)
	end = models.CharField(max_length=50, null=True)
	is_accept = models.BooleanField(default=False)
	is_incharge = models.BooleanField(default=False)
	is_head = models.BooleanField(default=False) 
	recieved = models.BooleanField(default=False) 

	def get_absolute_url(self):
		return reverse( 'retest:eventauditoriumform')
	def __str__(self):
				 return str(self.id)

class Eventmikesystem(models.Model):
	mike_system = models.ForeignKey(Mikesystems, limit_choices_to={'available': True},)
	date = models.DateField(blank=True, null=True)
	start = models.CharField(max_length=50, null=True)
	end = models.CharField(max_length=50, null=True)
	is_accept = models.BooleanField(default=False)
	is_incharge = models.BooleanField(default=False)
	is_head = models.BooleanField(default=False) 
	recieved = models.BooleanField(default=False) 
	def get_absolute_url(self):
		return reverse( 'retest:eventmikesystemform')
	def __str__(self):
				 return str(self.id)	

class Eventgraphicshall(models.Model):
	graphics_hall = models.ForeignKey(Graphicshalls, limit_choices_to={'available': True},)
	date = models.DateField(blank=True, null=True)
	start = models.CharField(max_length=50, null=True)
	end = models.CharField(max_length=50, null=True)
	is_accept = models.BooleanField(default=False)
	is_incharge = models.BooleanField(default=False)
	is_head = models.BooleanField(default=False) 
	recieved = models.BooleanField(default=False) 
	def get_absolute_url(self):
		return reverse( 'retest:eventgraphicshallform')
	def __str__(self):
				 return str(self.id)			 


