from email.mime import image
from email.policy import default
from random import choices
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    USER_GENDER_TYPE = (
        ('male', 'male'),
        ('female', 'female'),
        ('secret', 'secret'),
    )
    owner = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User')
    
    nick_name = models.CharField('nickname', max_length=20, blank=True, default='')
    birthday = models.DateField('birthday', null=True, blank=True)
    gender = models.CharField('gender', max_length=6, choices=USER_GENDER_TYPE, default='male')
    image = models.ImageField(upload_to='images/%y/%m', default='images/default.png', max_length=100, verbose_name='User image')
    level = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'User data'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.owner.username


class EmailVerifyRecord(models.Model):
    '''email verifycation record'''
    SEND_TYPE_CHOICE = (
        ('register','register'),
        ('forget','forget password'),
    )

    code = models.CharField('code', max_length=20)
    email = models.EmailField('email', max_length=35)
    send_type = models.CharField(choices=SEND_TYPE_CHOICE, default='register', max_length=20)

    class Meta:
        verbose_name = 'verification code'
        verbose_name_plural = verbose_name

    def __str__(self):
            return self.code
