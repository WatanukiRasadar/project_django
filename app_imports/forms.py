from django import forms
from .models import File

class ImportFileForm(forms.ModelForm):

    class Meta:
        model = File
        fields = ['filename']
        labels = {
            'file': 'Upload do Arquivo'
        }