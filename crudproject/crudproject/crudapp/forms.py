from . models import Crud
from django import forms

class Crudform(forms.ModelForm):
    class Meta:
        model=Crud
        fields=["slnumber","itemname","description"]