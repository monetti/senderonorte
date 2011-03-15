from django import forms
from django.forms.widgets import Textarea

# Create your forms here.
class ContactoForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    nombre_excursion = forms.CharField()
    fecha = forms.DateField()
    comentario = forms.CharField(required=False,widget=forms.Textarea)
