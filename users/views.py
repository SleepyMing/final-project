from multiprocessing import context
from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from .forms import LoginForm, RegisterForm, ForgetPwdForm, ChangePwdForm
from .models import EmailVerifyRecord
from utils.system_email_send import send_register_email

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

                send_register_email(form.cleaned_data.get('email'), 'register')

                return HttpResponse('nice to meet you')
    
    context = {'form' : form}
    return render(request, 'users/register.html',context) 

#If the user can be queried based on the verification code, 
#then activate the user and allow login to the background
def account_activate(request, active_code):
    all_records = EmailVerifyRecord.objects.filter(code=active_code)
    if all_records:
        for record in all_records:
            email = record.email
            user = User.objects.get(email=email)
            user.is_staff = True
            user.save
    else:
        return('wrong link!')
    return redirect('users:login')
            



class Mybackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None



def forget_pwd(request):
    if request.method == 'GET':
        form = ForgetPwdForm()
    elif request.method == 'POST':
        form = ForgetPwdForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            exists = User.objects.filter(email=email).exists()
            if exists:
                # send email
                send_register_email(email, 'forget')
                return HttpResponse('Email has been sent, please check！')
            else:
                return HttpResponse('Email has not been registered！')

    return render(request, 'users/forget_pwd.html', {'form': form})



def reset_pwd(request, active_code):
    if request.method != 'POST':
        form = ChangePwdForm()
    else:
        form = ChangePwdForm(request.POST)
        if form.is_valid():
            record = EmailVerifyRecord.objects.get(code=active_code)
            email = record.email
            user = User.objects.get(email=email)
            user.username = email
            user.password = make_password(form.cleaned_data.get('password'))
            user.save()
            return HttpResponse('Your Password Has Been Reset!')
        else:
            return HttpResponse('Fail to Reset Your Password')

    return render(request, 'users/reset_pwd.html', {'form': form})
