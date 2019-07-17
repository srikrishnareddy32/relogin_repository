from django import forms
from multiselectfield import MultiSelectFormField
class feedbackform(forms.Form):
    Name=forms.CharField(label='Enter your name',widget=forms.TextInput(attrs={'placeholder':'Name','class':'form-control','id':'name'}))
    Rating=forms.FloatField(label='Enter your rating',widget=forms.NumberInput(attrs={'placeholder':'Rating','class':'form-control','id':'rating'}))
    Feedback=forms.CharField(label='Enter your Feedback',widget=forms.Textarea(attrs={'placeholder':'Feedback','class':'form-control','id':'feedback'}))


class contactform(forms.Form):
    Name=forms.CharField(label='Enter your name',widget=forms.TextInput(attrs={'placeholder':'Name','class':'form-control','id':'name1'}))
    Email=forms.EmailField(label='Enter your Email',widget=forms.EmailInput(attrs={'placeholder':'Email','class':'form-control','id':'email'}))
    Mobile=forms.IntegerField(label='Enter your Number',widget=forms.NumberInput(attrs={'placeholder':'Number','class':'form-control','id':'number'}))
    JOB_LOCATION = (('hyd', 'hyderabad'), ('che', 'chennai'), ('mum', 'mumbai'), ('ban', 'bangalore'), ('pune', 'pune'))
    Location = MultiSelectFormField(max_length=30, choices=JOB_LOCATION)
    COURSES = (('PYTHON', 'PYTHON'), ('DJANGO', 'DJANGO'), ('UI', 'UI'), ('REST-API', 'REST-API'), ('JAVA', 'JAVA'))
    Course = MultiSelectFormField(max_length=20, choices=COURSES)
    GENDER=(('Male','Male'),('Female','Female'))
    Gender=forms.ChoiceField(widget=forms.RadioSelect(),choices=GENDER)
    y = range(1947, 2019)
    Dob=forms.DateField(label='Enter your DOB',widget=forms.SelectDateWidget(years=y))



