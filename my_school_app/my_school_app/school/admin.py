from django.contrib import admin
from .models import school, className, teacher, student

admin.site.register(school)
admin.site.register(className)
admin.site.register(teacher)
admin.site.register(student)
