from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=32)
    password = forms.CharField(label='password', min_length=6, widget=forms.PasswordInput())


# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = User
#         field = ('username', 'password')