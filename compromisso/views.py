from django.shortcuts import render
from .models import Compromisso


def hello_view(request):
    return render(request, 'base.html', {})


def list_compromissos(request):
    items = Compromisso.objects.all()
    return render(request, 'lista.html', {'items': items})    


def create_compromisso(request):
    if request.method == 'POST' 
        from CompromissoForm()
        return render()