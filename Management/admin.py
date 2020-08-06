from django.contrib import admin
from .models import WeeklyData,MidData,Student

# Register your models here.
admin.site.register(WeeklyData)
admin.site.register(MidData)
admin.site.register(Student)