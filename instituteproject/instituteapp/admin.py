from django.contrib import admin
from .models import coursesdata


class Admincoursesdata(admin.ModelAdmin):
    list_display = ['course_id','course_name','faculty_name','faculty_ex','course_fee','course_duration','starting_date','starting_time']


admin.site.register(coursesdata,Admincoursesdata)