from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
# Register your models here.

admin.site.unregister(User)

# 定义关联对象样式，stackedinline为纵向排列每一行
class UserprofileInline(admin.StackedInline):
    model = UserProfile

# 关联Userprofile
class UserProfileAdmin(UserAdmin):
    inlines = [UserprofileInline]


#注册User模型
admin.site.register(User, UserProfileAdmin)