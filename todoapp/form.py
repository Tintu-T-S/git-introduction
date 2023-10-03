from .models import players
from django import forms

class playersForm(forms.ModelForm):
    class Meta:
        model=players
        fields=['name','nationality','state','matches','runs','average','wickets','date']