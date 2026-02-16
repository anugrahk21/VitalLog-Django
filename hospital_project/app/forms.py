from django import forms
from django.forms import ModelForm
from .models import Patient

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'gender', 'address', 'phone_number', 'email', 'medical_history']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and not email.endswith('@gmail.com'):
            raise forms.ValidationError("Email must be from the domain '@gmail.com'")
        return email
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError("Phone number must contain only digits")
        return phone_number
    
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age and (age < 0 or age > 120):
            raise forms.ValidationError("Age must be between 0 and 120")
        return age
    
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        if name and len(name) < 2:
            raise forms.ValidationError("Name must be at least 2 characters long")
        
        return cleaned_data

