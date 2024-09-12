from django import forms
from .models import Sala, Reserva


class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['nome', 'descricao', 'situacao']

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['sala', 'data', 'horario_inicio', 'horario_termino']



