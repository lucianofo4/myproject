from django.shortcuts import render, redirect
from myapp.models import Name

# Create your views here.


def index(request):
    names_from_db = Name.objects.filter(hora="m")

    context_dict = {'names_from_context': names_from_db}
    return render(request, 'index.html', context_dict)


def tarde(request):
    names_from_db = Name.objects.filter(hora="t")

    context_dict = {'names_from_context': names_from_db}
    return render(request, 'tarde.html', context_dict)


