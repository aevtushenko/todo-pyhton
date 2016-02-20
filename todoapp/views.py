from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django import forms
from django.utils import timezone
from django.template import loader
# Create your views here.

from django.http import HttpResponse

from .models import Task
from .models import User as u
from .forms import NameForm, TaskForm, LoginForm

def index(request):
    taskform = TaskForm()
    user = u()
    latest_question_list = Task.objects.filter(owner = user.id).order_by('-pub_date')
    login = ''
    context = {'latest_question_list': latest_question_list, 'login': login, 'user': user, 'taskform': taskform}
    return render(request, 'tasks/index.html', context)

def register(request):
    form = NameForm()
    context= {'form' : form}
    return render(request, 'tasks/register.html', context)
    
def login(request):
    form = LoginForm()
    context= {'form' : form}
    return render(request, 'tasks/login.html', context)
    
def registeruser(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
#        if (form.cleaned_data['hashed_password'] != form.cleaned_data['hashed_password2']):
 #               form = NameForm()
  #              error = 'Passwords don\'t match!'
   #             context= {'form' : form, 'error': error}
    #            return render(request, 'tasks/register.html', context)
        if form.is_valid():
            if (u.objects.filter(email = form.cleaned_data['email'])):
                form = NameForm()
                error = 'Such user exists!'
                context= {'form' : form, 'error': error}
                return render(request, 'tasks/register.html', context)
            if (form.cleaned_data['hashed_password'] != form.cleaned_data['hashed_password2']):
                form = NameForm()
                error = 'Password don\'t match!'
                context= {'form' : form, 'error': error}
                return render(request, 'tasks/register.html', context)
            user = u()
            user.email = form.cleaned_data['email']
            user.name = form.cleaned_data['name']
            user.hashed_password = form.cleaned_data['hashed_password']
            user.save()
            login = 'You have succesfully registered with credentials: \nname: ' + str(user.name) + '\ne-mail: '+str(user.email)+' ! Please proceed to log in'
        else:
            form = NameForm()
            error = 'Error!'
            context= {'form' : form, 'error': error}
            return render(request, 'tasks/register.html', context)
            
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    taskform = TaskForm()
    user = u()
    latest_question_list = Task.objects.filter(owner = user.id).order_by('-pub_date')
    context = {'latest_question_list': latest_question_list, 'login': login, 'user': user, 'taskform': taskform}
    return render(request, 'tasks/index.html', context)
    
    
def loginuser(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            user = u.objects.get(email = form.cleaned_data['email'])
            print user
            print user.hashed_password
            print form.cleaned_data['hashed_password']
            if (user.hashed_password == form.cleaned_data['hashed_password']):
                taskform = TaskForm()
                
                latest_question_list = Task.objects.filter(owner = user.id).order_by('-pub_date')
                login = ''
                context = {'latest_question_list': latest_question_list, 'login': login, 'user': user, 'taskform': taskform}
                return render(request, 'tasks/index.html', context)
            else:
                form = LoginForm()
                error = 'Error!'
                context= {'form' : form, 'error': error}
                return render(request, 'tasks/login.html', context)
        else:
            form = LoginForm()
            error = 'Wrong Password!'
            context= {'form' : form, 'error': error}
            return render(request, 'tasks/login.html', context)
            
    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()
    taskform = TaskForm()
    user = u()    
    latest_question_list = Task.objects.filter(owner = user.id).order_by('-pub_date')
    login = ''
    context = {'latest_question_list': latest_question_list, 'login': login, 'user': user, 'taskform': taskform}
    return render(request, 'tasks/index.html', context)

    
    
    
    
def createtask(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print 0
        # create a form instance and populate it with data from the request:
        form = TaskForm(request.POST)
        useremail = str(request.POST.get('user',None))
        print type(useremail)
        # check whether it's valid:
        if form.is_valid():
            print 1
            
            user = u.objects.get(email = useremail)    
            task = Task()
            task.owner = user
            task.title = form.cleaned_data['title']
            task.description = form.cleaned_data['description']
            task.collaborators = form.cleaned_data['collaborator1'] + ' ' + form.cleaned_data['collaborator2'] + ' ' + form.cleaned_data['collaborator3']
            task.isComplete = False
            task.pub_date = timezone.now()
            task.save()
            taskform = TaskForm()
               
            latest_question_list = Task.objects.filter(owner = user.id).order_by('-pub_date')
            login = ''
            context = {'latest_question_list': latest_question_list, 'login': login, 'taskform': taskform, 'user': user}
            return render(request, 'tasks/index.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        print 2

    return render(request, 'tasks/index.html', {'form': form, 'user': user})
    
    
def deletetask(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print 0
        # create a form instance and populate it with data from the request:
        user1 = request.POST.get('user',None)
        print user1
        user = u.objects.get(email = str(user1))
        
        task1 = request.POST.get('task',None)
        print task1
        task = Task.objects.get(title = str(task1))
        task.delete()
        taskform = TaskForm()
        latest_question_list = Task.objects.filter(owner = user.id).order_by('-pub_date')
        for q in latest_question_list:
            print q.isComplete
        login = ''
        context = {'latest_question_list': latest_question_list, 'login': login, 'taskform': taskform, 'user': user}
        return render(request, 'tasks/index.html', context)
        
        
  

    return render(request, 'tasks/index.html', {'user': user})
    
def completetask(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print 0
        # create a form instance and populate it with data from the request:
        user1 = request.POST.get('user',None)
        print user1
        user = u.objects.get(email = str(user1))
        
        task1 = request.POST.get('task',None)
        print task1
        task = Task.objects.get(title = str(task1))
        print task.isComplete
        task.isComplete = not(task.isComplete)
        print task.isComplete
        task.save()
        taskform = TaskForm()
        latest_question_list = Task.objects.filter(owner = user.id).order_by('-pub_date')
 #       collaborator_list = Task.objects.raw(select * from Tasks where collaborators like %str(user.email)%)
  #      latest_question_list += collaborator_list
        for q in latest_question_list:
            print q.isComplete
        login = ''
        context = {'latest_question_list': latest_question_list, 'login': login, 'taskform': taskform, 'user': user}
        return render(request, 'tasks/index.html', context)
        
        
  

    return render(request, 'tasks/index.html', {'user': user})