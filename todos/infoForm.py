
from django import forms
class InfoForm(forms.Form):
    image = forms.ImageField(label='Image', help_text='Upload an image', required=True)