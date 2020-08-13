from django.shortcuts import render, get_object_or_404

from Backend.models import CMS, Praesidium


def index(request):

    return render(request, 'Jormungandr/index.html', {})


def cms(request, page):
    page = get_object_or_404(CMS, name=page)
    return render(request, 'Jormungandr/cms.html', {'page': page})


def praesidium(request):
    praesidium = Praesidium.objects.all()
    return render(request, 'Jormungandr/praesidium.html', {'praesidium': praesidium})


