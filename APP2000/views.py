from django.shortcuts import render,redirect
from django.http import HttpResponse 

def home(request):
	return render(request,'APP2000/home.html')