from django import forms
from .models import FormData

class FormDataForm(forms.ModelForm):
    class Meta:
        model = FormData
        fields = ['p_name', 'p_email', 'car_name','seats_available']
