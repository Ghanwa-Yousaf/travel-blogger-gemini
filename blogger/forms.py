from django import forms

class UploadForm(forms.Form):
    input_text = forms.CharField(label='Input', required=False, max_length=500)
    image = forms.ImageField(label='Upload image', required=True, allow_empty_file=False)
