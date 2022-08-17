from genericpath import exists
from tkinter import Widget
from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label = '', max_length=32,widget=forms.TextInput(attrs={'class': 'input', 'placeholder':'please enter your username/email'}))
    password = forms.CharField(label='', min_length=6, widget=forms.PasswordInput(attrs={'class': 'input','placeholder':'please enter your password'}))



class RegisterForm(forms.ModelForm):
    email = forms.EmailField(label = '', max_length=32,widget=forms.TextInput(attrs={'class': 'input', 'placeholder':'please enter your email'}))
    password = forms.CharField(label = '', min_length=6, widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder':'please enter your password'}))
    password1 = forms.CharField(label = '', min_length=6, widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder':'please enter your password agian'}))


    class Meta:
        model = User
        fields = ( 'email', 'password')

    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        exists = User.objects.filter(email=email).exists()
        if exists:
            raise forms.ValidationError('this email has already been registered')
        return email

    def clean_password1(self):
        if self.cleaned_data['password'] != self.cleaned_data['password1']:
            raise forms.ValidationError('The passwords entered twice do not match!')
        return self.cleaned_data['password1']
