from django import forms
from .models import Compromisso


class CompromissoForm(forms.ModelForm):
    class Meta:
        model = Compromisso
        fields = ('data', 'descricao', 'local', 'dress_code')