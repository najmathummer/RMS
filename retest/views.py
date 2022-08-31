#!/usr/bin/python -tt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import UserForm
from django.contrib.auth.models import User, Group
from .models import Departement, Semester, Subject, Batch, Retest, Classroom, Labs, Auditoriums, Graphicshalls, Mikesystems, Projectors, Extension_cables, Eventprojector, Eventlab, Eventextensioncable, Eventclassroom, Eventauditorium, Eventmikesystem, Eventgraphicshall, HeadofDept, Rep, allusers
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse

def logout_user(request):
    logout(request)
    print("entered")
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'retest/login.html', context)




    
def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        
        

        if user is not None:
            u = User.objects.get(username=username)
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'retest/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'retest/login.html', {'error_message': 'Invalid login'})
    return render(request, 'retest/login.html')
@login_required(login_url='/login')
def home(request):
    user = request.user
    if user.groups.filter(name='hod').exists():
        u = request.user
        projector_requests = Eventprojector.objects.all()
        lab_requests = Eventlab.objects.all()
        extensioncable_requests = Eventextensioncable.objects.all()
        all_requests= Retest.objects.all() 
        return render(request, 'retest/hod.html', {'u' : u, 'all_requests' : all_requests, 'extensioncable_requests' : extensioncable_requests, 'projector_requests': projector_requests, 'lab_requests' : lab_requests})
    elif user.groups.filter(name='principal').exists():
        u = request.user
        projector_requests = Eventprojector.objects.all()
        classroom_requests = Eventclassroom.objects.all()
        lab_requests = Eventlab.objects.all()
        mikesystem_requests = Eventmikesystem.objects.all()
        extensioncable_requests = Eventextensioncable.objects.all()
        auditorium_requests = Eventauditorium.objects.all()
        graphicshall_requests = Eventgraphicshall.objects.all()
        all_requests= Retest.objects.all() 
        return render(request, 'retest/principal.html', {'all_requests' : all_requests, 'extensioncable_requests' : extensioncable_requests ,'graphicshall_requests' : graphicshall_requests ,'auditorium_requests' : auditorium_requests, 'mikesystem_requests' : mikesystem_requests, 'projector_requests': projector_requests, 'lab_requests' : lab_requests, 'classroom_requests' : classroom_requests, 'u':u })
    elif user.groups.filter(name='Rep').exists():
        u = request.user
        all_requests= Retest.objects.all() 
        return render(request, 'retest/home.html', {'u':u, 'all_requests' : all_requests })
    elif user.groups.filter(name='Ajithzen').exists():
        u = request.user
        mikesystem_requests = Eventmikesystem.objects.all()
        extensioncable_requests = Eventextensioncable.objects.all()
        auditorium_requests = Eventauditorium.objects.all()
        return render(request, 'event/ajithzen.html', {'extensioncable_requests' : extensioncable_requests, 'auditorium_requests' : auditorium_requests, 'mikesystem_requests':mikesystem_requests, 'u':u })
    elif user.groups.filter(name='graphics').exists():
        u = request.user
        lab_requests = Eventlab.objects.all()
        graphicshall_requests = Eventgraphicshall.objects.all()
        return render(request, 'event/ashok.html', {'graphicshall_requests': graphicshall_requests, 'u':u,  'lab_requests' : lab_requests}) 
    elif user.groups.filter(name='Event_incharge').exists():
        u = request.user
        projector_requests = Eventprojector.objects.all()
        classroom_requests = Eventclassroom.objects.all()
        lab_requests = Eventlab.objects.all()
        mikesystem_requests = Eventmikesystem.objects.all()
        extensioncable_requests = Eventextensioncable.objects.all()
        auditorium_requests = Eventauditorium.objects.all()
        graphicshall_requests = Eventgraphicshall.objects.all()
        return render(request, 'event/incharge.html', { 'extensioncable_requests' : extensioncable_requests , 'projector_requests': projector_requests, 'lab_requests' : lab_requests, 'u' : u, 'classroom_requests':classroom_requests, 'auditorium_requests' : auditorium_requests, 'mikesystem_requests':mikesystem_requests, 'graphicshall_requests': graphicshall_requests})
    elif user.groups.filter(name='Event_coord').exists():
        u = request.user
        projector_requests = Eventprojector.objects.all()
        classroom_requests = Eventclassroom.objects.all()
        lab_requests = Eventlab.objects.all()
        mikesystem_requests = Eventmikesystem.objects.all()
        extensioncable_requests = Eventextensioncable.objects.all()
        auditorium_requests = Eventauditorium.objects.all()
        graphicshall_requests = Eventgraphicshall.objects.all()
        return render(request, 'event/chair.html', { 'extensioncable_requests' : extensioncable_requests ,'graphicshall_requests' : graphicshall_requests ,'auditorium_requests' : auditorium_requests, 'mikesystem_requests' : mikesystem_requests, 'projector_requests': projector_requests, 'lab_requests' : lab_requests, 'classroom_requests' : classroom_requests , 'u' : u})
    elif user.groups.filter(name='IEEE').exists():
        u = request.user
        projector_requests = Eventprojector.objects.all()
        extensioncable_requests = Eventextensioncable.objects.all()
        return render(request, 'event/ieee.html', { 'extensioncable_requests' : extensioncable_requests , 'projector_requests': projector_requests, 'u' : u})
    else:       
        return redirect('/login')
'''@login_required
def rep(request):
    u = request.user
    all_requests= Retest.objects.all() 
    return render(request, 'retest/home.html', {'u':u, 'all_requests' : all_requests })
@login_required
def hod(request):
    u = request.user
    projector_requests = Eventprojector.objects.all()
    lab_requests = Eventlab.objects.all()
    extensioncable_requests = Eventextensioncable.objects.all()
    all_requests= Retest.objects.all() 
    return render(request, 'retest/hod.html', {'u' : u, 'all_requests' : all_requests, 'extensioncable_requests' : extensioncable_requests, 'projector_requests': projector_requests, 'lab_requests' : lab_requests})
@login_required
def principal(request):
    u = request.user
    projector_requests = Eventprojector.objects.all()
    classroom_requests = Eventclassroom.objects.all()
    lab_requests = Eventlab.objects.all()
    mikesystem_requests = Eventmikesystem.objects.all()
    extensioncable_requests = Eventextensioncable.objects.all()
    auditorium_requests = Eventauditorium.objects.all()
    graphicshall_requests = Eventgraphicshall.objects.all()
    all_requests= Retest.objects.all() 
    return render(request, 'retest/principal.html', {'all_requests' : all_requests, 'extensioncable_requests' : extensioncable_requests ,'graphicshall_requests' : graphicshall_requests ,'auditorium_requests' : auditorium_requests, 'mikesystem_requests' : mikesystem_requests, 'projector_requests': projector_requests, 'lab_requests' : lab_requests, 'classroom_requests' : classroom_requests, 'u':u })
@login_required
def ajithsen(request):
    u = request.user
    mikesystem_requests = Eventmikesystem.objects.all()
    extensioncable_requests = Eventextensioncable.objects.all()
    auditorium_requests = Eventauditorium.objects.all()
    return render(request, 'event/ajithzen.html', {'extensioncable_requests' : extensioncable_requests, 'auditorium_requests' : auditorium_requests, 'mikesystem_requests':mikesystem_requests, 'u':u })
@login_required
def incharge(request):
    u = request.user
    projector_requests = Eventprojector.objects.all()
    classroom_requests = Eventclassroom.objects.all()
    lab_requests = Eventlab.objects.all()
    mikesystem_requests = Eventmikesystem.objects.all()
    extensioncable_requests = Eventextensioncable.objects.all()
    auditorium_requests = Eventauditorium.objects.all()
    graphicshall_requests = Eventgraphicshall.objects.all()
    return render(request, 'event/incharge.html', { 'extensioncable_requests' : extensioncable_requests , 'projector_requests': projector_requests, 'lab_requests' : lab_requests, 'u' : u, 'classroom_requests':classroom_requests, 'auditorium_requests' : auditorium_requests, 'mikesystem_requests':mikesystem_requests, 'graphicshall_requests': graphicshall_requests})
@login_required
def chair(request):
    u = request.user
    projector_requests = Eventprojector.objects.all()
    classroom_requests = Eventclassroom.objects.all()
    lab_requests = Eventlab.objects.all()
    mikesystem_requests = Eventmikesystem.objects.all()
    extensioncable_requests = Eventextensioncable.objects.all()
    auditorium_requests = Eventauditorium.objects.all()
    graphicshall_requests = Eventgraphicshall.objects.all()
    return render(request, 'event/chair.html', { 'extensioncable_requests' : extensioncable_requests ,'graphicshall_requests' : graphicshall_requests ,'auditorium_requests' : auditorium_requests, 'mikesystem_requests' : mikesystem_requests, 'projector_requests': projector_requests, 'lab_requests' : lab_requests, 'classroom_requests' : classroom_requests , 'u' : u})
@login_required
def ieee(request):
    u = request.user
    projector_requests = Eventprojector.objects.all()
    extensioncable_requests = Eventextensioncable.objects.all()
    return render(request, 'event/ieee.html', { 'extensioncable_requests' : extensioncable_requests , 'projector_requests': projector_requests, 'u' : u})
@login_required
def ashok(request):
    u = request.user
    lab_requests = Eventlab.objects.all()
    graphicshall_requests = Eventgraphicshall.objects.all()
    return render(request, 'event/ashok.html', {'graphicshall_requests': graphicshall_requests, 'u':u,  'lab_requests' : lab_requests}) '''

    
@login_required
def details(request, retest_id):
    try:
        retest= Retest.objects.get(pk=retest_id)
    except Retest.DoesNotExist:
        raise Http404("Request does not exit")
    return render(request, 'retest/details.html' , { 'retest': retest })

class RetestCreate(CreateView):
    model = Retest
    fields = ['semester', 'dept', 'batch', 'date', 'subject', 'name', 'admnno', 'reason', 'proof', 'is_sure']
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
    
    try:
        retest= Retest.objects.get(pk=retest_id)
    except Retest.DoesNotExist:
        raise Http404("Request does not exit")
    return render(request, 'retest/request.html' , { 'retest': retest})

@login_required
def accepted(request, retest_id):
    retest = get_object_or_404(Retest, pk=retest_id)
    if request.method == 'POST':
        retest.is_principal = True
        retest.save(update_fields=['is_principal'])

        users = [rep.user for rep in Rep.objects.filter(batch=retest.batch, dept=retest.dept)]
        for user in users:
            user.email_user(subject='RMS', message='Your Notifications are Pending')

    return render(request, 'retest/request.html' , {'retest': retest})


@login_required
def retreq(request, retest_id):
   
    try:
        retest= Retest.objects.get(pk=retest_id)
    except Retest.DoesNotExist:
        raise Http404("Request does not exit")
    return render(request, 'retest/retreq.html' , { 'retest': retest })

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



def ashokindetails(request, eventgraphicshall_id):
    a = User.objects.get(username='gokul')
    try:
        eventgraphicshall= Eventgraphicshall.objects.get(pk=eventgraphicshall_id)
    except Eventgraphicshall.DoesNotExist:
        raise Http404("Request does not exit")    
    return render(request, 'event/ashokindetails.html', { 'eventgraphicshall' : eventgraphicshall , 'a' : a  })



def iaccept(request, eventgraphicshall_id):
    eventgraphicshall = get_object_or_404(Eventgraphicshall, pk=eventgraphicshall_id)
    if request.method == 'POST':
        eventgraphicshall.is_incharge = True
        eventgraphicshall.save(update_fields=['is_incharge'])
        
    return render(request, 'event/ashokindetails.html' , {'eventgraphicshall' : eventgraphicshall })

def ashokhdetails(request, eventgraphicshall_id):
    a = User.objects.get(username='gokul')
    try:
        eventgraphicshall= Eventgraphicshall.objects.get(pk=eventgraphicshall_id)
    except Eventgraphicshall.DoesNotExist:
        raise Http404("Request does not exit")    
    return render(request, 'event/ashokhdetails.html', { 'eventgraphicshall' : eventgraphicshall , 'a' : a  })
def haccept(request, eventgraphicshall_id):
    eventgraphicshall = get_object_or_404(Eventgraphicshall, pk=eventgraphicshall_id)
    if request.method == 'POST':
        eventgraphicshall.is_head = True
        eventgraphicshall.save(update_fields=['is_head'])
    return render(request, 'event/ashokhdetails.html' , {'eventgraphicshall' : eventgraphicshall })

def ashokdetails(request, eventgraphicshall_id):
    a = User.objects.get(username='gokul')
    try:
        eventgraphicshall= Eventgraphicshall.objects.get(pk=eventgraphicshall_id)
    except Eventgraphicshall.DoesNotExist:
        raise Http404("Request does not exit")    
    return render(request, 'event/ashokdetails.html', { 'eventgraphicshall' : eventgraphicshall , 'a' : a  })
def gaccept(request, eventgraphicshall_id):
    eventgraphicshall = get_object_or_404(Eventgraphicshall, pk=eventgraphicshall_id)
    if request.method == 'POST':
        eventgraphicshall.is_accept = True
        eventgraphicshall.save(update_fields=['is_accept'])
        if eventgraphicshall.is_accept == True :
            eventgraphicshall.graphics_hall.available = False
            eventgraphicshall.graphics_hall.save(update_fields=['available'])
    return render(request, 'event/ashokdetails.html' , {'eventgraphicshall' : eventgraphicshall })


def ashokretreq(request, eventgraphicshall_id):
    a = User.objects.get(username='gokul')
    try:
        eventgraphicshall= Eventgraphicshall.objects.get(pk=eventprojector_id)
    except Eventgraphicshall.DoesNotExist:
        raise Http404("Request does not exit")
    return render(request, 'event/ashokretereq.html' , { 'eventgraphicshall' : eventgraphicshall , 'a' : a })
def ashokwretreq(request, eventgraphicshall_id):
    a = User.objects.get(username='gokul')
    try:
        eventgraphicshall= Eventgraphicshall.objects.get(pk=eventgraphicshall_id)
    except Eventgraphicshall.DoesNotExist:
        raise Http404("Request does not exit")
    return render(request, 'event/ashokwretereq.html' , { 'eventgraphicshall' : eventgraphicshall , 'a' : a })
def graphicswithdraw(request, eventgraphicshall_id):
    eventgraphicshall = get_object_or_404(Eventgraphicshall, pk=eventgraphicshall_id)
    if request.method == 'POST':
        eventgraphicshall.recieved = True
        eventgraphicshall.save(update_fields=['recieved'])
        if eventgraphicshall.recieved == True :
            eventgraphicshall.graphics_hall.available = True
            eventgraphicshall.graphics_hall.save(update_fields=['available'])
    return render(request, 'event/ashokretereq.html' , {'eventgraphicshall' : eventgraphicshall })


def projectorindetails(request, eventprojector_id):
    a = User.objects.get(username='gokul')
    try:
        eventprojector= Eventprojector.objects.get(pk=eventprojector_id)
    except Eventprojector.DoesNotExist:
        raise Http404("Request does not exit")    
    return render(request, 'event/projectorindetails.html', { 'eventprojector' : eventprojector , 'a' : a  })

def iprojectoraccept(request, eventprojector_id):
    eventprojector = get_object_or_404(Eventprojector, pk=eventprojector_id)
    if request.method == 'POST':
        eventprojector.is_incharge = True
        eventprojector.save(update_fields=['is_incharge'])
    return render(request, 'event/projectorindetails.html' , {'eventprojector' : eventprojector})

def projectorhdetails(request, eventprojector_id):
    a = User.objects.get(username='gokul')
    try:
        eventprojector= Eventprojector.objects.get(pk=eventprojector_id)
    except Eventprojector.DoesNotExist:
        raise Http404("Request does not exit")    
    return render(request, 'event/projectorhdetails.html' , { 'eventprojector' : eventprojector , 'a' : a  })

def hprojectoraccept(request, eventprojector_id):
    eventprojector = get_object_or_404(Eventprojector, pk=eventprojector_id)
    if request.method == 'POST':
        eventprojector.is_head = True
        eventprojector.save(update_fields=['is_head'])
        
    return render(request, 'event/projectorhdetails.html' , {'eventprojector' : eventprojector})

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
        eventprojector.is_accept = True
        eventprojector.save(update_fields=['is_accept'])
        if eventprojector.is_accept == True:
            eventprojector.projector.available = False
            eventprojector.projector.save(update_fields=['available'])
    return render(request, 'event/projectordetails.html' , {'eventprojector' : eventprojector})

def projectorretreq(request, eventprojector_id):
    a = User.objects.get(username='gokul')
    try:
        eventprojector= Eventprojector.objects.get(pk=eventprojector_id)
    except Eventprojector.DoesNotExist:
        raise Http404("Request does not exit")
    return render(request, 'event/projectorretreq.html' , { 'eventprojector' : eventprojector , 'a' : a })

def projectorhretreq(request, eventprojector_id):
    a = User.objects.get(username='gokul')
    try:
        eventprojector= Eventprojector.objects.get(pk=eventprojector_id)
    except Eventprojector.DoesNotExist:
        raise Http404("Request does not exit")
    return render(request, 'event/projectorhretreq.html' , { 'eventprojector' : eventprojector , 'a' : a })
def projectorrecieved(request, eventprojector_id):
    eventprojector = get_object_or_404(Eventprojector, pk=eventprojector_id)
    if request.method == 'POST':
        eventprojector.recieved = True
        eventprojector.save(update_fields=['recieved'])
        if eventprojector.recieved == True:
            eventprojector.projector.available = True
            eventprojector.projector.save(update_fields=['available'])
    return render(request, 'event/projectorretreq.html' , {'eventprojector' : eventprojector})




def labdetails(request, eventlab_id):
    a = User.objects.get(username='gokul')
    try:
        eventlab= Eventlab.objects.get(pk=eventlab_id)
    except Eventlab.DoesNotExist:
        raise Http404("Request does not exit")    
    return render(request, 'event/labdetails.html' , { 'eventlab' : eventlab , 'a' : a  })

def labaccept(request, eventlab_id):
    eventlab = get_object_or_404(Eventlab, pk=eventlab_id)
    if request.method == 'POST':
        eventlab.is_accept = True
        eventlab.save(update_fields=['is_accept'])
        if eventlab.is_accept == True:
            eventlab.lab.available = False
            eventlab.lab.save(update_fields=['available'])
    return render(request, 'event/labdetails.html' , {'eventlab' : eventlab})

def labindetails(request, eventlab_id):
    a = User.objects.get(username='gokul')
    try:
        eventlab= Eventlab.objects.get(pk=eventlab_id)
    except Eventlab.DoesNotExist:
        raise Http404("Request does not exit")    
    return render(request, 'event/labindetails.html' , { 'eventlab' : eventlab , 'a' : a  })

def ilabaccept(request, eventlab_id):
    eventlab = get_object_or_404(Eventlab, pk=eventlab_id)
    if request.method == 'POST':
        eventlab.is_incharge = True
        eventlab.save(update_fields=['is_incharge'])
    return render(request, 'event/labindetails.html' , {'eventlab' : eventlab})

def labhdetails(request, eventlab_id):
    a = User.objects.get(username='gokul')
    try:
        eventlab= Eventlab.objects.get(pk=eventlab_id)
    except Eventlab.DoesNotExist:
        raise Http404("Request does not exit")    
    return render(request, 'event/labhdetails.html' , { 'eventlab' : eventlab , 'a' : a  })

def hlabaccept(request, eventlab_id):
    eventlab = get_object_or_404(Eventlab, pk=eventlab_id)
    if request.method == 'POST':
        eventlab.is_head = True
        eventlab.save(update_fields=['is_head'])
        
    return render(request, 'event/labhdetails.html' , {'eventlab' : eventlab})

def labretreq(request, eventlab_id):
    a = User.objects.get(username='gokul')
    try:
        eventlab= Eventlab.objects.get(pk=eventlab_id)
    except Eventlab.DoesNotExist:
        raise Http404("Request does not exit")
    return render(request, 'event/labretreq.html' , { 'eventlab' : eventlab , 'a' : a })
def labwretreq(request, eventlab_id):
    a = User.objects.get(username='gokul')
    try:
        eventlab= Eventlab.objects.get(pk=eventlab_id)
    except Eventlab.DoesNotExist:
        raise Http404("Request does not exit")
    return render(request, 'event/labwretreq.html' , { 'eventlab' : eventlab , 'a' : a })
def labwithdraw(request, eventlab_id):
    eventlab = get_object_or_404(Eventlab, pk=eventlab_id)
    if request.method == 'POST':
        eventlab.recieved = True
        eventlab.save(update_fields=['recieved'])
        if eventlab.recieved == True:
            eventlab.lab.available = True
            eventlab.lab.save(update_fields=['available'])
    return render(request, 'event/labretreq.html' , {'eventlab' : eventlab})




def auditoriumindetails(request, eventauditorium_id):
    a = User.objects.get(username='gokul')
    try:
        eventauditorium= Eventauditorium.objects.get(pk=eventauditorium_id)
    except Eventauditorium.DoesNotExist:
        raise Http404("Request does not exit")    
    return render(request, 'event/auditoriumindetails.html' , { 'eventauditorium' : eventauditorium , 'a' : a  })

def iauditoriumaccept(request, eventauditorium_id):
    eventauditorium = get_object_or_404(Eventauditorium, pk=eventauditorium_id)
    if request.method == 'POST':
        eventauditorium.is_incharge = True
        eventauditorium.save(update_fields=['is_incharge'])
    return render(request, 'event/auditoriumindetails.html' , {'eventauditorium' : eventauditorium})

def auditoriumhdetails(request, eventauditorium_id):
    a = User.objects.get(username='gokul')
    try:
        eventauditorium= Eventauditorium.objects.get(pk=eventauditorium_id)
    except Eventauditorium.DoesNotExist:
        raise Http404("Request does not exit")    
    return render(request, 'event/auditoriumhdetails.html' , { 'eventauditorium' : eventauditorium , 'a' : a  })

def hauditoriumaccept(request, eventauditorium_id):
    eventauditorium = get_object_or_404(Eventauditorium, pk=eventauditorium_id)
    if request.method == 'POST':
        eventauditorium.is_head = True
        eventauditorium.save(update_fields=['is_head'])
    return render(request, 'event/auditoriumhdetails.html' , {'eventauditorium' : eventauditorium})

def auditoriumdetails(request, eventauditorium_id):
    a = User.objects.get(username='gokul')
    try:
        eventauditorium= Eventauditorium.objects.get(pk=eventauditorium_id)
    except Eventauditorium.DoesNotExist:
        raise Http404("Request does not exit")    
    return render(request, 'event/auditoriumdetails.html' , { 'eventauditorium' : eventauditorium , 'a' : a  })

def auditoriumaccept(request, eventauditorium_id):
    eventauditorium = get_object_or_404(Eventauditorium, pk=eventauditorium_id)
    if request.method == 'POST':
        eventauditorium.is_accept = True
        eventauditorium.save(update_fields=['is_accept'])
        if eventauditorium.is_accept == True:
            eventauditorium.auditorium.available = False
            eventauditorium.auditorium.save(update_fields=['available'])
    return render(request, 'event/auditoriumdetails.html' , {'eventauditorium' : eventauditorium})

def auditretreq(request, eventauditorium_id):
    a = User.objects.get(username='gokul')
    try:
        eventauditorium= Eventauditorium.objects.get(pk=eventauditorium_id)
    except Eventauditorium.DoesNotExist:
        raise Http404("Request does not exit")
    return render(request, 'event/auditretereq.html' , { 'eventauditorium' : eventauditorium , 'a' : a })
def auditwretreq(request, eventauditorium_id):
    a = User.objects.get(username='gokul')
    try:
        eventauditorium= Eventauditorium.objects.get(pk=eventauditorium_id)
    except Eventauditorium.DoesNotExist:
        raise Http404("Request does not exit")
    return render(request, 'event/auditwretereq.html' , { 'eventauditorium' : eventauditorium , 'a' : a })
def auditwithdraw(request, eventauditorium_id):
    eventauditorium = get_object_or_404(Eventauditorium, pk=eventauditorium_id)
    if request.method == 'POST':
        eventauditorium.recieved = True
        eventauditorium.save(update_fields=['recieved'])
        if eventauditorium.recieved == True:
            eventauditorium.auditorium.available = True
            eventauditorium.auditorium.save(update_fields=['available'])
    return render(request, 'event/auditretereq.html' , {'eventauditorium' : eventauditorium})



def mikedetails(request, eventmikesystem_id):
    a = User.objects.get(username='gokul')
    try:
        eventmikesystem= Eventmikesystem.objects.get(pk=eventmikesystem_id)
    except Eventmikesystem.DoesNotExist:
        raise Http404("Request does not exit")    
    return render(request, 'event/mikedetails.html' , { 'eventmikesystem' : eventmikesystem , 'a' : a  })

def mikeaccept(request, eventmikesystem_id):
    eventmikesystem = get_object_or_404(Eventmikesystem, pk=eventmikesystem_id)
    if request.method == 'POST':
        eventmikesystem.is_accept = True
        eventmikesystem.save(update_fields=['is_accept'])
        if eventmikesystem.is_accept == True:
            eventmikesystem.mike_system.available = False
            eventmikesystem.mike_system.save(update_fields=['available'])
    return render(request, 'event/mikedetails.html' , {'eventmikesystem' : eventmikesystem})

def mikeindetails(request, eventmikesystem_id):
    a = User.objects.get(username='gokul')
    try:
        eventmikesystem= Eventmikesystem.objects.get(pk=eventmikesystem_id)
    except Eventmikesystem.DoesNotExist:
        raise Http404("Request does not exit")    
    return render(request, 'event/mikeindetails.html' , { 'eventmikesystem' : eventmikesystem , 'a' : a  })

def imikeaccept(request, eventmikesystem_id):
    eventmikesystem = get_object_or_404(Eventmikesystem, pk=eventmikesystem_id)
    if request.method == 'POST':
        eventmikesystem.is_incharge = True
        eventmikesystem.save(update_fields=['is_incharge'])
        return render(request, 'event/mikeindetails.html' , {'eventmikesystem' : eventmikesystem})
def mikehdetails(request, eventmikesystem_id):
    a = User.objects.get(username='gokul')
    try:
        eventmikesystem= Eventmikesystem.objects.get(pk=eventmikesystem_id)
    except Eventmikesystem.DoesNotExist:
        raise Http404("Request does not exit")    
    return render(request, 'event/mikehdetails.html' , { 'eventmikesystem' : eventmikesystem , 'a' : a  })

def hmikeaccept(request, eventmikesystem_id):
    eventmikesystem = get_object_or_404(Eventmikesystem, pk=eventmikesystem_id)
    if request.method == 'POST':
        eventmikesystem.is_head = True
        eventmikesystem.save(update_fields=['is_head'])
        
    return render(request, 'event/mikehdetails.html' , {'eventmikesystem' : eventmikesystem})

def mikeretreq(request, eventmikesystem_id):
    a = User.objects.get(username='gokul')
    try:
        eventmikesystem= Eventmikesystem.objects.get(pk=eventmikesystem_id)
    except Eventmikesystem.DoesNotExist:
        raise Http404("Request does not exit")
    return render(request, 'event/mikeretreq.html' , { 'eventmikesystem' : eventmikesystem , 'a' : a })

def mikehretreq(request, eventmikesystem_id):
    a = User.objects.get(username='gokul')
    try:
        eventmikesystem= Eventmikesystem.objects.get(pk=eventmikesystem_id)
    except Eventmikesystem.DoesNotExist:
        raise Http404("Request does not exit")
    return render(request, 'event/mikehretreq.html' , { 'eventmikesystem' : eventmikesystem , 'a' : a })
def mikerecieved(request, eventmikesystem_id):
    eventmikesystem = get_object_or_404(Eventmikesystem, pk=eventmikesystem_id)
    if request.method == 'POST':
        eventmikesystem.recieved = True
        eventmikesystem.save(update_fields=['recieved'])
        if eventmikesystem.recieved == True:
            eventmikesystem.mike_system.available = True
            eventmikesystem.mike_system.save(update_fields=['available'])
    return render(request, 'event/mikeretreq.html' , {'eventmikesystem' : eventmikesystem})



def classroomdetails(request, eventclassroom_id):
    a = User.objects.get(username='gokul')
    try:
        eventclassroom= Eventclassroom.objects.get(pk=eventclassroom_id)
    except Eventclassroom.DoesNotExist:
        raise Http404("Request does not exit")    
    return render(request, 'event/classroomdetails.html' , { 'eventclassroom' : eventclassroom , 'a' : a  })

def classroomaccept(request, eventclassroom_id):
    eventclassroom = get_object_or_404(Eventclassroom, pk=eventclassroom_id)
    if request.method == 'POST':
        eventclassroom.is_accept = True
        eventclassroom.save(update_fields=['is_accept'])
        if eventclassroom.is_accept == True:
            eventclassroom.classroom.available = False
            eventclassroom.classroom.save(update_fields=['available'])
    return render(request, 'event/classroomdetails.html' , {'eventclassroom' : eventclassroom})
def classroomidetails(request, eventclassroom_id):
    a = User.objects.get(username='gokul')
    try:
        eventclassroom= Eventclassroom.objects.get(pk=eventclassroom_id)
    except Eventclassroom.DoesNotExist:
        raise Http404("Request does not exit")    
    return render(request, 'event/classroomidetails.html' , { 'eventclassroom' : eventclassroom , 'a' : a  })

def iclassroomaccept(request, eventclassroom_id):
    eventclassroom = get_object_or_404(Eventclassroom, pk=eventclassroom_id)
    if request.method == 'POST':
        eventclassroom.is_incharge = True
        eventclassroom.save(update_fields=['is_incharge'])
        
    return render(request, 'event/classroomidetails.html' , {'eventclassroom' : eventclassroom})

        
def classretreq(request, eventclassroom_id):
    a = User.objects.get(username='gokul')
    try:
        eventclassroom= Eventclassroom.objects.get(pk=eventclassroom_id)
    except Eventclassroom.DoesNotExist:
        raise Http404("Request does not exit")
    return render(request, 'event/classretreq.html' , { 'eventclassroom' : eventclassroom , 'a' : a })
def classwretreq(request, eventclassroom_id):
    a = User.objects.get(username='gokul')
    try:
        eventclassroom= Eventclassroom.objects.get(pk=eventclassroom_id)
    except Eventclassroom.DoesNotExist:
        raise Http404("Request does not exit")
    return render(request, 'event/classwretreq.html' , { 'eventclassroom' : eventclassroom , 'a' : a })
def classwithdraw(request, eventclassroom_id):
    eventclassroom = get_object_or_404(Eventclassroom, pk=eventclassroom_id)
    if request.method == 'POST':
        eventclassroom.recieved = True
        eventclassroom.save(update_fields=['recieved'])
        if eventclassroom.recieved == True:
            eventclassroom.classroom.available = True
            eventclassroom.classroom.save(update_fields=['available'])
    return render(request, 'event/classretreq.html' , {'eventclassroom' : eventclassroom})



def cabledetails(request, eventextensioncable_id):
    a = User.objects.get(username='gokul')
    try:
        eventextensioncable= Eventextensioncable.objects.get(pk=eventextensioncable_id)
    except Eventprojector.DoesNotExist:
        raise Http404("Request does not exit")    
    return render(request, 'event/cabledetails.html' , { 'eventextensioncable' : eventextensioncable , 'a' : a  })

def cableaccept(request, eventextensioncable_id):
    eventextensioncable = get_object_or_404(Eventextensioncable, pk=eventextensioncable_id)
    if request.method == 'POST':
        eventextensioncable.is_accept = True
        eventextensioncable.save(update_fields=['is_accept'])
        if eventextensioncable.is_accept == True:
            eventextensioncable.extension_cable.available = False
            eventextensioncable.extension_cable.save(update_fields=['available'])
    return render(request, 'event/cabledetails.html' , {'eventextensioncable' : eventextensioncable})
def cableindetails(request, eventextensioncable_id):
    a = User.objects.get(username='gokul')
    try:
        eventextensioncable= Eventextensioncable.objects.get(pk=eventextensioncable_id)
    except Eventprojector.DoesNotExist:
        raise Http404("Request does not exit")    
    return render(request, 'event/cableindetails.html' , { 'eventextensioncable' : eventextensioncable , 'a' : a  })

def icableaccept(request, eventextensioncable_id):
    eventextensioncable = get_object_or_404(Eventextensioncable, pk=eventextensioncable_id)
    if request.method == 'POST':
        eventextensioncable.is_incharge = True
        eventextensioncable.save(update_fields=['is_incharge'])
        
    return render(request, 'event/cableindetails.html' , {'eventextensioncable' : eventextensioncable})
def cablehdetails(request, eventextensioncable_id):
    a = User.objects.get(username='gokul')
    try:
        eventextensioncable= Eventextensioncable.objects.get(pk=eventextensioncable_id)
    except Eventprojector.DoesNotExist:
        raise Http404("Request does not exit")    
    return render(request, 'event/cablehdetails.html' , { 'eventextensioncable' : eventextensioncable , 'a' : a  })

def hcableaccept(request, eventextensioncable_id):
    eventextensioncable = get_object_or_404(Eventextensioncable, pk=eventextensioncable_id)
    if request.method == 'POST':
        eventextensioncable.is_head = True
        eventextensioncable.save(update_fields=['is_head'])
        if eventextensioncable.is_accept == True:
            eventextensioncable.extension_cable.available = False
            eventextensioncable.extension_cable.save(update_fields=['available'])
    return render(request, 'event/cablehdetails.html' , {'eventextensioncable' : eventextensioncable})

def cableretreq(request, eventextensioncable_id):
    a = User.objects.get(username='gokul')
    try:
        eventextensioncable= Eventextensioncable.objects.get(pk=eventextensioncable_id)
    except Eventextensioncable.DoesNotExist:
        raise Http404("Request does not exit")
    return render(request, 'event/cableretreq.html' , { 'eventextensioncable' : eventextensioncable , 'a' : a })
def cablehretreq(request, eventextensioncable_id):
    a = User.objects.get(username='gokul')
    try:
        eventextensioncable= Eventextensioncable.objects.get(pk=eventextensioncable_id)
    except Eventextensioncable.DoesNotExist:
        raise Http404("Request does not exit")
    return render(request, 'event/cablehretreq.html' , { 'eventextensioncable' : eventextensioncable , 'a' : a })
def cablerecieved(request, eventextensioncable_id):
    eventextensioncable = get_object_or_404(Eventextensioncable, pk=eventextensioncable_id)
    if request.method == 'POST':
        eventextensioncable.recieved = True
        eventextensioncable.save(update_fields=['recieved'])
        if eventextensioncable.recieved == True:
            eventextensioncable.extension_cable.available = True
            eventextensioncable.extension_cable.save(update_fields=['available'])
    return render(request, 'event/cableretreq.html' , {'eventextensioncable' : eventextensioncable})
