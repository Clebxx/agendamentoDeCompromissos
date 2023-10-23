from django import forms
from .models import Compromisso


class CompromissoForm(form.Form): 
    class Meta:
        model = Compromisso