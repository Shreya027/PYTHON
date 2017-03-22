from django.shortcuts import render

# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from wiki.forms import StudentForm
from .models import Student
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required














def index(request):
    return render(request,'index.html')    

def question1(request):
    return render(request,'qr1.html')       

def question2(request):
    return render(request,'qr2.html')  

def question3(request):
    return render(request,'qr3.html')  

def question4(request):
    return render(request,'qr4.html')  

def question5(request):
    return render(request,'qr5.html')  

def question6(request):
    return render(request,'qr6.html')      

def end(request):
    
    return render(request,'end.html')  


def index(request):

    if request.method == 'POST':
        form = StudentForm(request.POST ,request.FILES or None )
        if form.is_valid():
            cd = form.cleaned_data
            Student.objects.create(name=cd['name'],team_name=cd['team_name'],sap_id=cd['sap_id'],branch=cd['branch'],year=cd['year'])
        form = StudentForm()    
        return render(request,'qr1.html')               
    else:
        form = StudentForm()
    return render(request, 'index.html', {'form': form})  







































