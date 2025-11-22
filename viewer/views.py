from django.shortcuts import render
#from django.views.generic import *
#from viewer.models import Information




def home(request):
    return render(request,'base.html')