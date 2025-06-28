from django.contrib import admin
from .models import Manager, Intern, Address

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'department')

@admin.register(Intern)
class InternAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'mentor', 'internship_end')

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'city', 'state', 'content_object')

# Superuser details (add as comment)
# Email:ukpraise14@gmail.com
# Password: Praise

