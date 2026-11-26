
from django import forms

class PersonForm(forms.Form):
    name = forms.CharField(label = "Name" , max_length = 100 , required = True)
    age = forms.IntegerField(label = "Age" , required = True)
    job = forms.CharField(label = "Job" , max_length = 100 , required = True)