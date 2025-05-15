from django.shortcuts import render, get_object_or_404
from .models import Service

# Create your views here.

def service_list(request):
    services = Service.objects.all()
    return render(request, 'services/service_list.html', {'services': services})

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    related_services = Service.objects.exclude(id=service.id)[:3]  # Get up to 3 related services
    
    context = {
        'service': service,
        'related_services': related_services,
    }
    return render(request, 'services/service_detail.html', context)
