from multiprocessing import context
from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .forms import LoginForm, RegisterForm


# Create your views here.


def user_login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method != 'POST':
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username = username, password = password)
        
            if user is not None:
                login(request, user)
                return HttpResponse('Welcome!')
            else:
                return HttpResponse('Invalid login details supplied.')
    context = {'form': form}
    return render(request, 'users/login.html',context)


def Register(request):
    if request.method != 'POST':
        form = RegisterForm()
    else:
            form = RegisterForm(request.POST)
            if form.is_valid():
                new_user = form.save(commit=False)
                new_user.set_password(form.cleaned_data.get('password'))
                new_user.username = form.cleaned_data.get('email')
                new_user.save()
                return HttpResponse('nice to meet you')
    
    context = {'form' : form}
    return render(request, 'users/register.html',context) 

    

# def login_register(request):
#     # If the request is a HTTP POST, try to pull out the relevant information.
#     if request.method == 'POST':

#         if request.POST.get('submit') == 'signup':
#             form = RegisterForm(request.POST)
#             if form.is_valid():
#                 new_user = form.save(commit=False)
#                 new_user.set_password(form.cleaned_data.get('password'))
#                 new_user.save()
#                 return HttpResponse('nice to meet you')

#             context = {'form': form}    

#         if request.POST.get('submit') == 'login':
#             form = LoginForm(request.POST)
#             if form.is_valid():
#                 username = form.cleaned_data['username']
#                 password = form.cleaned_data['password']
#                 user = authenticate(request, username = username, password = password)
        
#                 if user is not None:
#                     login(request, user)
#                     return HttpResponse('Welcome!')
#                 else:
#                     return HttpResponse('Invalid login details supplied.')

#             context = {'form': form}

#     # context = context
#     return render(request, 'users/index.html', context) 


class Mybackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None
        