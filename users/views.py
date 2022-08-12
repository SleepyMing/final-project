from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

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
    return render(request, 'users/index.html',context)


def register(request):
    if request.method != 'POST':
        pass
    else:
        pass

    return render(request, 'users/register.html') 
    

def login_register(request):
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
    return render(request, 'users/index.html',context) 