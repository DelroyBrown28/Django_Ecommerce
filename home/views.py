from django.shortcuts import render
from .models import HomePageCustomisation


def index(request):
    home_page_customisation = HomePageCustomisation.objects.all()
    context = {
        'home_page_customisation' : home_page_customisation,

    }
    return render(request, 'home/index.html', context)


def NavbarCustomisation(request):
    navbar_customisation = NavbarCustomisation.objects.all()
    context = {
        'navbar_customisation' : navbar_customisation,

    }
    return render(request, 'includes/main_nav.html', context)
