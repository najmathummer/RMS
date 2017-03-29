#!/usr/bin/python -tt
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import UserForm
from django.contrib.auth.models import User, Group
from .models import Departement, Semester, Subject, Batch, Retest, CustomUser
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.shortcuts import get_list_or_404, get_object_or_404


    
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        all_requests= Retest.objects.all()
        
        
        

        if user is not None:
            if user.is_active:
                login(request, user)
                if user.groups.filter(name='hod').exists():
                	users = CustomUser.objects.get(username=username)
                	return render(request, 'retest/hod.html', {'all_requests' : all_requests,'users':users})
                elif user.groups.filter(name='principal').exists():
                	return render(request, 'retest/principal.html', {'all_requests' : all_requests})
                elif user.groups.filter(name='Rep').exists():
                	users = CustomUser.objects.get(username=username)
                	return render(request, 'retest/home.html', {'all_requests' : all_requests,'users':users})
                else:		
                	return render(request, 'retest/login.html', {'error_message': 'Invalid login'})

            else:
                return render(request, 'retest/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'retest/login.html', {'error_message': 'Invalid login'})
    return render(request, 'retest/login.html')

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
def accept(request, retest_id):
    retest = get_object_or_404(Retest, pk=retest_id)
    # update is_hod attribute only if the request is a POST.
    if request.method == 'POST':
        retest.is_hod = True
        retest.save(update_fields=['is_hod'])
    return render(request, 'retest/details.html' , {'retest': retest})
def request(request, retest_id):
    a = User.objects.get(username='Varghese')
    try:
        retest= Retest.objects.get(pk=retest_id)
    except Retest.DoesNotExist:
        raise Http404("Request does not exit")
    return render(request, 'retest/request.html' , { 'retest': retest , 'a' : a })

def accepted(request, retest_id):
    retest = get_object_or_404(Retest, pk=retest_id)
    # update is_hod attribute only if the request is a POST.
    if request.method == 'POST':
        retest.is_principal = True
        retest.save(update_fields=['is_principal'])
    return render(request, 'retest/request.html' , {'retest': retest})

def retreq(request, retest_id):
    a = User.objects.get(username='Varghese')
    try:
        retest= Retest.objects.get(pk=retest_id)
    except Retest.DoesNotExist:
        raise Http404("Request does not exit")
    return render(request, 'retest/retreq.html' , { 'retest': retest , 'a' : a })
