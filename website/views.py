from django.shortcuts import render
from apps.services.models import Service

# Create your views here.

def landing_page(request):
    featured_services = Service.objects.filter(initial_page=True)
    return render(request, 'pages/landing.html', {'featured_services': featured_services})
