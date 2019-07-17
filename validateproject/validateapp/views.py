from django.shortcuts import render
from .forms import RegistrationForm
from .models import RegistrationData

def RegForm_Page(request):
    form = RegistrationForm(request.POST or None)
    context = {
        'form' : form
    }

    if form.is_valid():
        print(form.cleaned_data)

        firstname = form.cleaned_data.get('firstname')
        lastname = form.cleaned_data.get('lastname')
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password1 = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')
        mobile = form.cleaned_data.get('mobile')

        data = RegistrationData(firstname=firstname,lastname=lastname,username=username,email=email,password1=password1,
            password2=password2,
            mobile=mobile
        )
        data.save()

    return render(request,'feedback.html' , context)