from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
# Register your models here.

User = get_user_model()

admin.site.unregister(Group)

@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ('name', 'email', 'company_name', 'website_name', 'profession', 'is_staff')
    
    list_filter = ('is_staff', 'profession',)