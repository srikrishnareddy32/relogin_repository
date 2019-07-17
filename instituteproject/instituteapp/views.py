from django.shortcuts import render,redirect
from .models import feedbackdata,contactdata,coursesdata
from .forms import feedbackform,contactform
import datetime
from django.http.response import HttpResponse
Date=datetime.datetime.now()
def base(request):
    return render(request,'base.html')
def home(request):
    return render(request,'home.html')


def contacts(request):
    if request.method=='POST':
        cform1=contactform(request.POST)
        if cform1.is_valid():
            Name=cform1.cleaned_data.get('Name')
            Email=cform1.cleaned_data.get('Email')
            Mobile=cform1.cleaned_data.get('Mobile')
            Location=cform1.cleaned_data.get('Location')
            Course=cform1.cleaned_data.get('Course')
            Gender=cform1.cleaned_data.get('Gender')
            Dob=cform1.cleaned_data.get('Dob')
            data=contactdata(Name=Name,Email=Email,Mobile=Mobile,Location=Location,Course=Course,Gender=Gender,Dob=Dob)
            data.save()
            cform1=contactform()
            return render(request,'contact.html',{'cform1':cform1})
        else:
            return HttpResponse('inavild')
    else:
        cform1=contactform()
        return render(request,'contact.html',{'cform1':cform1})
def course(request):
    course=coursesdata.objects.all()
    return render(request,'course.html',{'course':course})
def feedback(request):
    if request.method=="POST":
        fb=feedbackform(request.POST)
        if fb.is_valid():
            Name=request.POST.get('Name','')
            Rating=request.POST.get('Rating','')
            Feedback=request.POST.get('Feedback','')
            fbdata=feedbackdata(Name=Name,Rating=Rating,Date=Date,Feedback=Feedback)
            fbdata.save()
            fb = feedbackform()
            ab=feedbackdata.objects.all()
            return render(request, 'feedback.html', {'fb': fb,'ab':ab})
        else:
            ab = feedbackdata.objects.all()
            fb = feedbackform()
            return render(request, 'feedback.html', {'fb': fb, 'ab': ab})
    else:
        ab = feedbackdata.objects.all()
        fb=feedbackform()
        return render(request,'feedback.html',{'fb': fb,'ab':ab})
def team(request):
    return render(request,'team.html')
def gallery(request):
    return render(request,'gallery.html')