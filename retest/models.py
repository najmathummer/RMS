#!/usr/bin/python -tt
from django.db import models



class Departement(models.Model):
	dept = models.CharField(max_length=50)
	hod = models.ForeignKey('auth.User')
	def __str__(self):
				 return self.dept
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
	admnno = models.CharField(max_length=50, primary_key=True)
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
	admnno = models.ForeignKey(Student)
	reason = models.CharField(max_length=50)
	proof = models.CharField(max_length=200)
	def __str__(self):
				 return self.name
	
	