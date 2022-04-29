from django.contrib import admin

# Register your models here.

from app.models import Schoolbranch,Eighth,ExamModel
admin.site.register(Schoolbranch)
admin.site.register(Eighth)
admin.site.register(ExamModel)