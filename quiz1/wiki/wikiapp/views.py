from django.shortcuts import render

# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render,redirect

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

def question7(request):
    return render(request,'qr7.html') 

def question8(request):
    return render(request,'qr8.html') 

def question9(request):
    return render(request,'qr9.html') 

def question10(request):
    return render(request,'qr10.html') 

def question11(request):
    return render(request,'qr11.html') 

def question12(request):
    return render(request,'qr12.html')   


def question13(request):
    return render(request,'qr13.html') 


def question14(request):
    return render(request,'qr14.html')  




def end(request):
    
    return render(request,'end.html')  


def index(request):

       
    return render(request, 'index.html')  







































