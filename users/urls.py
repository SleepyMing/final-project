from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # path('login.html', views.user_login, name='login'),
    # path('register.html', views.register, name='register'),
    path('index.html', views.login_register, name='index'),
]