from django import forms
from django.forms import widgets
from webapp.models import STATUS_LS_CHOICES as list


class TaskForm(forms.Form):
    title = forms.CharField(max_length=200, required=True, label='Title')
    status = forms.ChoiceField(choices=list, required=False, label='Status')
    description = forms.CharField(max_length=3000, required=True, label='Description', widget=widgets.Textarea)
    created_at = forms.DateField(label='Date', initial=None, required=False, widget=widgets.DateInput(attrs={'type': 'date'}))
