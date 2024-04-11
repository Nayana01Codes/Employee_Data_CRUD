from django.contrib import admin
from .models import Employee

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["name","email","contact","dept","gender","salary",'image']

admin.site.register(Employee,EmployeeAdmin)