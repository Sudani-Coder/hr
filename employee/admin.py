from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['Fname', 'Minit', 'Lname', 'ssn', 'Bdate', 'Address', 'Sex', 'Salary', 'Super_ssn', 'dno']
    search_fields = ["ssn"]

admin.site.register(Employee, EmployeeAdmin)

''' Unregistered Models '''

# admin.site.unregister(User)
# admin.site.unregister(Group)
