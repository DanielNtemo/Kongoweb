
from django.views.generic import ListView

from viewer.models import Information


# Create your tests here.

class InformationView(ListView):
    model = Information
    context_object_name = 'informations'
    template_name = 'information.html'
