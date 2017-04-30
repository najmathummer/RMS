#!/usr/bin/python -tt
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import UserForm
from django.contrib.auth.models import User, Group
from .models import Departement, Semester, Subject, Batch, Retest, CustomUser, Classroom, Labs, Auditoriums, Graphicshalls, Mikesystems, Projectors, Extension_cables, Eventprojector, Eventlab, Eventextensioncable, Eventclassroom, Eventauditorium, Eventmikesystem, Eventgraphicshall
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'retest/login.html', context)




    
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        all_requests= Retest.objects.all() 
        projector_requests = Eventprojector.objects.all()
        classroom_requests = Eventclassroom.objects.all()
        lab_requests = Eventlab.objects.all()
        mikesystem_requests = Eventmikesystem.objects.all()
        extensioncable_requests = Eventextensioncable.objects.all()
        auditorium_requests = Eventauditorium.objects.all()
        graphicshall_requests = Eventgraphicshall.objects.all()
        
        
        
        

        if user is not None:
            if user.is_active:
                login(request, user)
                if user.groups.filter(name='hod').exists():
                	users = CustomUser.objects.get(username=username)
                	return render(request, 'retest/hod.html', {'all_requests' : all_requests, 'users':users, 'extensioncable_requests' : extensioncable_requests, 'graphicshall_requests' : graphicshall_requests, 'auditorium_requests' : auditorium_requests, 'mikesystem_requests' : mikesystem_requests, 'projector_requests': projector_requests, 'lab_requests' : lab_requests, 'classroom_requests' : classroom_requests })
                elif user.groups.filter(name='principal').exists():
                	return render(request, 'retest/principal.html', {'all_requests' : all_requests, 'extensioncable_requests' : extensioncable_requests ,'graphicshall_requests' : graphicshall_requests ,'auditorium_requests' : auditorium_requests, 'mikesystem_requests' : mikesystem_requests, 'projector_requests': projector_requests, 'lab_requests' : lab_requests, 'classroom_requests' : classroom_requests})
                elif user.groups.filter(name='Rep').exists():
                	users = CustomUser.objects.get(username=username)
                	return render(request, 'retest/home.html', {'all_requests' : all_requests,'users':users})
                elif user.groups.filter(name='Ajithzen').exists():
                    
                    return render(request, 'event/ajithzen.html', {})
                elif user.groups.filter(name='graphics').exists():
                    
                    return render(request, 'event/ashok.html', {})    
                elif user.groups.filter(name='Event_incharge').exists():
                    users = CustomUser.objects.get(username=username)
                    return render(request, 'event/event_incharge.html', { 'extensioncable_requests' : extensioncable_requests , 'projector_requests': projector_requests, 'lab_requests' : lab_requests, 'users' : users})
                elif user.groups.filter(name='Event_coord').exists():
                    users = CustomUser.objects.get(username=username)
                    return render(request, 'event/chair.html', { 'extensioncable_requests' : extensioncable_requests ,'graphicshall_requests' : graphicshall_requests ,'auditorium_requests' : auditorium_requests, 'mikesystem_requests' : mikesystem_requests, 'projector_requests': projector_requests, 'lab_requests' : lab_requests, 'classroom_requests' : classroom_requests , 'users' : users,})
                elif user.groups.filter(name='IEEE').exists():
                    users = CustomUser.objects.get(username=username)
                    return render(request, 'event/event_incharge.html', { 'extensioncable_requests' : extensioncable_requests , 'projector_requests': projector_requests, 'lab_requests' : lab_requests, 'users' : users})
                else:		
                	return render(request, 'retest/login.html', {'error_message': 'Invalid login'})

            else:
                return render(request, 'retest/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'retest/login.html', {'error_message': 'Invalid login'})
    return render(request, 'retest/login.html')
@login_required
def details(request, retest_id):
    a = User.objects.get(username='Varghese')
    try:
        retest= Retest.objects.get(pk=retest_id)
    except Retest.DoesNotExist:
        raise Http404("Request does not exit")
    return render(request, 'retest/details.html' , { 'retest': retest , 'a' : a })

class RetestCreate(CreateView):
    model = Retest
    fields = ['semester', 'dept', 'batch', 'date', 'subject', 'name', 'admnno', 'reason', 'proof']
@login_required
def accept(request, retest_id):
    retest = get_object_or_404(Retest, pk=retest_id)
    # update is_hod attribute only if the request is a POST.
    if request.method == 'POST':
        retest.is_hod = True
        retest.save(update_fields=['is_hod'])
    return render(request, 'retest/details.html' , {'retest': retest})
@login_required
def request(request, retest_id):
    a = User.objects.get(username='Varghese')
    try:
        retest= Retest.objects.get(pk=retest_id)
    except Retest.DoesNotExist:
        raise Http404("Request does not exit")
    return render(request, 'retest/request.html' , { 'retest': retest , 'a' : a })

@login_required
def accepted(request, retest_id):
    retest = get_object_or_404(Retest, pk=retest_id)
    # update is_hod attribute only if the request is a POST.
    if request.method == 'POST':
        retest.is_principal = True
        retest.save(update_fields=['is_principal'])
        email = EmailMessage('Hello', 'World', to=['najmathu8@gmail.com'])
        email.send()
    return render(request, 'retest/request.html' , {'retest': retest})
@login_required
def retreq(request, retest_id):
    a = User.objects.get(username='Varghese')
    try:
        retest= Retest.objects.get(pk=retest_id)
    except Retest.DoesNotExist:
        raise Http404("Request does not exit")
    return render(request, 'retest/retreq.html' , { 'retest': retest , 'a' : a })

def homepage(request):
    return render(request, 'retest/rms.html', {})

class EventextensioncableCreate(CreateView):
    model = Eventextensioncable
    fields = ['extension_cable' , 'date', 'start', 'end' ]


class EventprojectorCreate(CreateView):
    model = Eventprojector
    fields = ['projector' , 'date', 'start', 'end']


class EventlabCreate(CreateView):
    model = Eventlab
    fields = ['lab' , 'date', 'start', 'end']


class EventclassroomCreate(CreateView):
    model = Eventclassroom
    fields = ['classroom' , 'date', 'start', 'end'] 

class EventauditoriumCreate(CreateView):
    model = Eventauditorium
    fields = ['auditorium' , 'date', 'start', 'end']       

class EventmikesystemCreate(CreateView):
    model = Eventmikesystem
    fields = ['mike_system' , 'date', 'start', 'end']

class EventgraphicshallCreate(CreateView):
    model = Eventgraphicshall
    fields = ['graphics_hall' , 'date', 'start', 'end']


"""def inchargedetails(request, events_id):
    a = User.objects.get(username='GokulG')
    try:
        event= Events.objects.get(pk=events_id)
    except Events.DoesNotExist:
        raise Http404("Request does not exit")
    return render(request, 'event/inchargedetails.html' , { 'event': event , 'a' : a })

def inchargeaccept(request, events_id):
    event = get_object_or_404(Events, pk=events_id)
    # update is_hod attribute only if the request is a POST.
    if request.method == 'POST':
        event.is_incharge = True
        event.save(update_fields=['is_incharge'])
    return render(request, 'event/inchargedetails.html' , {'event': event})

def hoddetails(request, eventhod_id):
    a = User.objects.get(username='GokulG')
    try:
        event= Eventhod.objects.get(pk=eventhod_id)
    except Eventhod.DoesNotExist:
        raise Http404("Request does not exit")
    return render(request, 'event/hoddetails.html' , { 'event': event , 'a' : a })

def hodaccept(request, eventhod_id):
    event = get_object_or_404(Eventhod, pk=eventhod_id)
    if request.method == 'POST':
        event.is_hod = True
        event.save(update_fields=['is_hod'])
    return render(request, 'event/hoddetails.html' , {'event': event})


def ajithzendetails(request, eventajithzen_id):
    a = User.objects.get(username='GokulG')
    try:
        event= Eventajithzen.objects.get(pk=eventajithzen_id)
    except Eventajithzen.DoesNotExist:
        raise Http404("Request does not exit")
    return render(request, 'event/ajithzendetails.html' , { 'event': event , 'a' : a })

def ajithzenaccept(request, eventajithzen_id):
    event = get_object_or_404(Eventajithzen, pk=eventajithzen_id)
    if request.method == 'POST':
        event.is_hod = True
        event.save(update_fields=['is_ajithzen'])
    return render(request, 'event/ajithzendetails.html' , {'event': event})"""


def ashokdetails(request, eventgraphicshall_id):
    a = User.objects.get(username='Gokul')
    try:
        eventgraphicshall= Eventgraphicshall.objects.get(pk=eventgraphicshall_id)
    except Eventgraphicshall.DoesNotExist:
        raise Http404("Request does not exit")
    return render(request, 'event/ashokdetails.html' , { 'eventgraphicshall' : eventgraphicshall , 'a' : a })

def ashokaccept(request, eventgraphicshall_id):
    eventgraphicshall = get_object_or_404(Eventgraphicshall, pk=eventgraphicshall_id)
    if request.method == 'POST':
        eventgraphicshall.is_accept = eventgraphicshall.is_accept+1
        eventgraphicshall.save(update_fields=['is_accept'])
    return render(request, 'event/ashokdetails.html' , {'eventgraphicshall' : eventgraphicshall })



"""def principaldetails(request, event_id):
   a = User.objects.get(username='GokulG')
   try:
       event= Events.objects.get(pk=events_id)
   except Events.DoesNotExist:
       raise Http404("Request does not exit")
   return render(request, 'event/principaldetails.html' , { 'event': event , 'a' : a })


def principalaccept(request, event_id):
    event = get_object_or_404(Events, pk=events_id)
    # update is_hod attribute only if the request is a POST.
    if request.method == 'POST':
        event.is_hod = True
        event.save(update_fields=['is_principal'])
    return render(request, 'event/principaldetails.html' , {'event': event})


def eventretreq(request, event_id):
    a = User.objects.get(username='GokulG')
    try:
        event= Events.objects.get(pk=events_id)
    except Events.DoesNotExist:
        raise Http404("Request does not exit")
    return render(request, 'event/eventretreq.html' , { 'event': event , 'a' : a })"""




def projectordetails(request, eventprojector_id):
    a = User.objects.get(username='gokul')
    try:
        eventprojector= Eventprojector.objects.get(pk=eventprojector_id)
    except Eventprojector.DoesNotExist:
        raise Http404("Request does not exit")    
    return render(request, 'event/projectordetails.html' , { 'eventprojector' : eventprojector , 'a' : a  })

def projectoraccept(request, eventprojector_id):
    eventprojector = get_object_or_404(Eventprojector, pk=eventprojector_id)
    if request.method == 'POST':
        eventprojector.is_accept = eventprojector.is_accept+1
        eventprojector.save(update_fields=['is_accept'])

        if eventprojector.is_accept == 3:
            

            if eventprojector.projector.sec.sec_name == 'CS':
                eventprojector.projector.delete()
                
            elif eventprojector.projector.sec.sec_name == 'EC':
                eventprojector.projector.delete()
            
            elif eventprojector.projector.sec.sec_name == 'EEE':
                eventprojector.projector.delete()
            
            elif eventprojector.projector.sec.sec_name == 'IEEE':
                eventprojector.projector.delete()
            
            elif eventprojector.projector.sec.sec_name == 'TPC':
                eventprojector.projector.delete()
    return render(request, 'event/projectordetails.html' , {'eventprojector' : eventprojector })



def labdetails(request, eventlab_id):
    a = User.objects.get(username='Gokul')
    try:
        eventlab= Eventlab.objects.get(pk=eventlab_id)
    except Eventlab.DoesNotExist:
        raise Http404("Request does not exit")
    return render(request, 'event/labdetails.html' , { 'eventlab' : eventlab , 'a' : a })

def labaccept(request, eventlab_id):
    eventlab = get_object_or_404(Eventlab, pk=eventlab_id)
    if request.method == 'POST':
        eventlab.is_accept = eventlab.is_accept+1
        eventlab.save(update_fields=['is_accept'])
    return render(request, 'event/labdetails.html' , {'eventlab' : eventlab })



def auditoriumdetails(request, eventauditorium_id):
    a = User.objects.get(username='Gokul')
    try:
        eventauditorium= Eventauditorium.objects.get(pk=eventauditorium_id)
    except Eventauditorium.DoesNotExist:
        raise Http404("Request does not exit")
    return render(request, 'event/auditoriumdetails.html' , { 'eventauditorium' : eventauditorium , 'a' : a })

def auditoriumaccept(request, eventauditorium_id):
    eventauditorium = get_object_or_404(Eventauditorium, pk=eventauditorium_id)
    if request.method == 'POST':
        eventauditorium.is_accept = eventauditorium.is_accept+1
        eventauditorium.save(update_fields=['is_accept'])
    return render(request, 'event/auditoriumdetails.html' , {'eventauditorium' : eventauditorium })



def mikedetails(request, eventmikesystem_id):
    a = User.objects.get(username='Gokul')
    try:
        eventmikesystem= Eventmikesystem.objects.get(pk=eventmikesystem_id)
    except Eventmikesystem.DoesNotExist:
        raise Http404("Request does not exit")
    return render(request, 'event/mikedetails.html' , { 'eventmikesystem' : eventmikesystem , 'a' : a })

def mikeaccept(request, eventmikesystem_id):
    eventmikesystem = get_object_or_404(Eventmikesystem, pk=eventmikesystem_id)
    if request.method == 'POST':
        eventmikesystem.is_accept = eventmikesystem.is_accept+1
        eventmikesystem.save(update_fields=['is_accept'])
    return render(request, 'event/mikedetails.html' , {'eventmikesystem' : eventmikesystem })




def classroomdetails(request, eventclassroom_id):
    a = User.objects.get(username='Gokul')
    try:
        eventclassroom= Eventclassroom.objects.get(pk=eventclassroom_id)
    except Eventclassroom.DoesNotExist:
        raise Http404("Request does not exit")
    return render(request, 'event/classroomdetails.html' , { 'eventclassroom' : eventclassroom , 'a' : a })

def classroomaccept(request, eventclassroom_id):
    eventclassroom = get_object_or_404(Eventclassroom, pk=eventclassroom_id)
    if request.method == 'POST':
        eventclassroom.is_accept = eventclassroom.is_accept+1
        eventclassroom.save(update_fields=['is_accept'])
    return render(request, 'event/classroomdetails.html' , {'eventclassroom' : eventclassroom })



def cabledetails(request, eventextensioncable_id):
    a = User.objects.get(username='Gokul')
    try:
        eventextensioncable= Eventextensioncable.objects.get(pk=eventextensioncable_id)
    except Eventextensioncable.DoesNotExist:
        raise Http404("Request does not exit")
    return render(request, 'event/cabledetails.html' , { 'eventextensioncable' : eventextensioncable , 'a' : a })

def cableaccept(request, eventextensioncable_id):
    eventextensioncable = get_object_or_404(Eventextensioncable, pk=eventextensioncable_id)
    if request.method == 'POST':
        eventextensioncable.is_accept = eventextensioncable.is_accept+1
        eventextensioncable.save(update_fields=['is_accept'])
    return render(request, 'event/cabledetails.html' , {'eventextensioncable' : eventextensioncable })


