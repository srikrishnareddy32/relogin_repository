from django.db import models
from multiselectfield import MultiSelectField

class feedbackdata(models.Model):
    Name=models.CharField(max_length=20)
    Rating=models.FloatField()
    Date=models.DateTimeField()
    Feedback=models.TextField(max_length=300)

class contactdata(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField(max_length=30)
    Mobile=models.BigIntegerField()
    JOB_LOCATION=(('hyd','hyderabad'),('che','chennai'),('mum','mumbai'),('ban','bangalore'),('pune','pune'))
    Location=MultiSelectField(max_length=100,choices=JOB_LOCATION)
    COURSES=(('PYTHON','PYTHON'),('DJANGO','DJANGO'),('UI','UI'),('REST-API','REST-API'))
    Course=MultiSelectField(max_length=100,choices=COURSES)
    Gender=models.CharField(max_length=20)
    Dob=models.DateField(max_length=20)


class coursesdata(models.Model):
    course_id=models.IntegerField()
    course_name=models.CharField(max_length=30)
    faculty_name=models.CharField(max_length=30)
    faculty_ex=models.IntegerField()
    course_fee=models.IntegerField()
    course_duration=models.IntegerField()
    starting_date=models.DateField(max_length=30)
    starting_time=models.TimeField(max_length=30)



