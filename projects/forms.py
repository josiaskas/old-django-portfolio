from django import forms
from .models import Contact
class ContactForm(forms.Form):
    name = forms.CharField(
        label='Nom',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'input '}),
        required=True
        )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'input '}),
        required=True)
    
    project_type = forms.ChoiceField(
        label='Type of project', 
        choices=Contact.PROJECTS_TYPES, 
        required=True)

    amount = forms.FloatField(
        label = 'Budget',
        widget = forms.NumberInput(attrs={'class' : 'input','min':300}),
        required=True)
    
    details = forms.CharField(
        label='Additional details',
        max_length=1000,
        widget=forms.Textarea(attrs={'class':'textarea','rows':5}),
        required=True
        )