from django.contrib import admin
from course_introduction.models import Profile,RegisteredSubject 

# Register your models here.

class DesigProfileAdmin(admin.ModelAdmin):
    list_display = ["id","name"]
    list_per_page = 10
    list_filter=["id"]
    search_fields=["id"]
    

class DesigRegisterSubjectAdmin(admin.ModelAdmin):
    list_display = ["profile","idSubject","nameSubject"]
    list_per_page = 10
    list_filter=["profile"]
    search_fields = ["idSubject"]
    

admin.site.register(Profile,DesigProfileAdmin)
admin.site.register(RegisteredSubject,DesigRegisterSubjectAdmin)