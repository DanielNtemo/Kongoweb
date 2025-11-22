from django.shortcuts import render
from django.views.generic import *
from viewer.models import Information


class InformationView(ListView):
    model = Information
    context_object_name = 'information'
    template_name = 'information.html'

def home(request):
    return render(request,'base.html')