#!/usr/bin/python -tt
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import UserForm
from django.contrib.auth.models import User, Group
from .models import Departement, Semester, Subject, Batch, Retest
from django.contrib.auth.decorators import login_required


'''def group_required(group, login_url=None, raise_exception=False):
    """
    Decorator for views that checks whether a user has a group permission,
    redirecting to the log-in page if necessary.
    If the raise_exception parameter is given the PermissionDenied exception
    is raised.
    """
    
    groups = (group, )

    if user.groups.filter(name__in=groups).exists():
        return True
        # In case the 403 handler should be called raise the exception
    if raise_exception:
        raise PermissionDenied
        # As the last resort, show the login form
    return False'''
    
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        

        if user is not None:
            if user.is_active:
                login(request, user)
                if user.groups.filter(name='hod').exists():
                	return render(request, 'retest/hod.html', {})
                else:
                	if user.groups.filter(name='principal').exists():
                		return render(request, 'retest/hod.html', {})
                	else:
                		if user.groups.filter(name='Rep').exists():
                			return render(request, 'retest/home.html', {})
                		else:
                			return render(request, 'retest/login.html', {'error_message': 'Invalid login'})

                
                
                
            else:
                return render(request, 'retest/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'retest/login.html', {'error_message': 'Invalid login'})
    return render(request, 'retest/login.html')
@login_required(login_url='/retest/')
def retestform(request):
	dept = Departement.objects.all()
	sem = Semester.objects.all()
	sub = Subject.objects.all()
	div = Batch.objects.all()
	name = Retest.objects.all()
	date = Retest.objects.all()

	return render(request, 'retest/retestform.html', {'sem':sem, 'dept':dept, 'sub':sub, 'div':div})

# Create your views here.
