from django.contrib import admin

from .models import Departement, Semester, Subject, Student, Retest, Batch, CustomUser 
admin.site.register(Departement)
admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Retest)
admin.site.register(Batch)
admin.site.register(CustomUser) 
