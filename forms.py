from django import forms
from django.db import models

class UploadFileForm(forms.Form):
    file = forms.FileField("Archivo", widget=forms.FileInput)

