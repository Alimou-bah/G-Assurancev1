from django.contrib import admin
from users.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'last_name','first_name', 'is_active', 'is_staff')
    list_filter = ('is_staff', 'is_active')

admin.site.register(User, UserAdmin)