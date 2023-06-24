from django.contrib import admin
from .models import User, StudentsAdmission, ContactRequest

# Register your models here.
admin.site.register(User)
admin.site.register(StudentsAdmission)
admin.site.register(ContactRequest)
