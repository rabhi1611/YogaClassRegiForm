from django.contrib import admin

# Register your models here.
from .models import Month, Batch, Student

admin.site.register(Month)

admin.site.register(Batch)

admin.site.register(Student)
