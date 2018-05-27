from django import forms

class ImportFile(forms.Form):
    file = forms.FileField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['file'].label = "Upload do Arquivo"
        self.fields['file'].widget.attrs.update({'class': 'form-control-file'})