from django.shortcuts import render, redirect
from django.db.models import Q

from compromisso.forms import CompromissoForm
from compromisso.models import Compromisso



def hello_view(request):
    return render(request, 'base.html', {})


def list_compromissos(request):
    dados = {}
    query = request.GET.get('q')
    if query:
        dados['query'] = query
        queryset = (Q(data__icontains=query))
        items = Compromisso.objects.filter(queryset).distinct()
    else:
        items = Compromisso.objects.all()
    dados['items'] = items
    return render(request, 'lista.html', dados)


def create_compromisso(request):
    error = None
    if request.method == "POST":
        form = CompromissoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista-compromisso')
        error = 'Formulário mal formatado'
    form = CompromissoForm()
    return render(request, 'form.html', {'form': form, 'erro': error})

def edit_compromisso(request, pk):
    compromisso = Compromisso.objects.get(id=pk)
    if request.method == "POST":
        form = CompromissoForm(request.POST, instance=compromisso)
        if form.is_valid():
            form.save()
        return redirect('lista-compromisso')
    else:
        form = CompromissoForm(instance=compromisso)
        return render(request, 'form.html', {'form': form, 'pk': pk})


def delete_compromisso(request, pk):
    Compromisso.objects.get(id=pk).delete()
    return redirect('lista-compromisso')