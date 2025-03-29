from django import forms
from saloon.models import Record, Service, Employee, Client

class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['client','service', 'employee', 'record_date', 'record_time']
        widgets = {
            'service': forms.HiddenInput(),
            'employee': forms.HiddenInput(),
        }