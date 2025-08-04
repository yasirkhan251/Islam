from django.shortcuts import render, get_object_or_404
from .models import ServiceCategory


def home(request):
    categories = ServiceCategory.objects.all()
    return render(request, 'home.html', {'categories': categories})


def category_services(request, id):
    category = get_object_or_404(ServiceCategory, id=id)
    services = category.services.all()
    context = {'category': category, 'services': services}
    return render(request, 'category_services.html', context)
