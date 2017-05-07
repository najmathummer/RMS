from django.contrib import admin

from .models import Departement, Semester, Subject, Retest, Batch, Labs, Graphicshalls, Auditoriums, Projectors, Mikesystems, Extension_cables, Eventprojector, Eventlab, Eventextensioncable, Eventclassroom, Eventauditorium, Eventmikesystem, Eventgraphicshall, Section, Classroom, HeadofDept, Rep, allusers
admin.site.register(Departement)
admin.site.register(Semester)
admin.site.register(Subject)

admin.site.register(Retest)
admin.site.register(Batch)
#admin.site.register(CustomUser) 
admin.site.register(Classroom)
admin.site.register(Auditoriums)
admin.site.register(Graphicshalls)
admin.site.register(Labs)
admin.site.register(Projectors)
admin.site.register(Mikesystems)
admin.site.register(Extension_cables)
admin.site.register(Eventprojector)
admin.site.register(Eventlab)
admin.site.register(Eventextensioncable)
admin.site.register(Eventclassroom)
admin.site.register(Eventauditorium)
admin.site.register(Eventmikesystem)
admin.site.register(Eventgraphicshall)
admin.site.register(Section)
admin.site.register(HeadofDept)
admin.site.register(Rep)
admin.site.register(allusers)

