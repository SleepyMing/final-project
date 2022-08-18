from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.Register, name='register'),
    path('active/<active_code>', views.account_activate, name = 'account_activate'),
    path('forget_pwd/', views.forget_pwd, name = 'forget_pwd'),
    path('reset_pwd/<active_code>', views.reset_pwd, name='reset_pwd'),
]