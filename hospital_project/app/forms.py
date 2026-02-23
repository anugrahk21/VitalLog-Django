from django import forms
from django.forms import ModelForm
from .models import Patient
from django.contrib.auth.models import User # Built in user model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class PatientForm(ModelForm):
    class Meta:
        # Links this form to the 'Patient' model. 
        # Django will automatically generate form fields for the model fields defined here.
        model = Patient
        # Specifies exactly which fields from the model should be included in the form.
        fields = ['name', 'age', 'gender', 'address', 'phone_number', 'email', 'medical_history']
        
    # Validation for a specific field: 'email'
    # Django automatically looks for methods named 'clean_<fieldname>' and runs them.
    def clean_email(self):
        # self.cleaned_data contains data that has passed basic type checks (like "is this an email format?")
        email = self.cleaned_data.get('email')
        
        # Add custom logic: Check if it ends with @gmail.com
        if email and not email.endswith('@gmail.com'):
            raise forms.ValidationError("Email must be from the domain '@gmail.com'")
            
        # You MUST return the value (cleaned or modified) at the end of the method
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
    
    # General validation for the entire form.
    # This runs AFTER all individual 'clean_<fieldname>' methods have finished.
    # It is useful for validations that involve multiple fields (e.g. "password" matches "confirm_password")
    def clean(self):
        # Get the dictionary of data that has passed all previous checks
        cleaned_data = super().clean()
        
        # You can access any field here
        name = cleaned_data.get('name')
        
        # Example validation: Check if name is too short
        if name and len(name) < 2:
            raise forms.ValidationError("Name must be at least 2 characters long")
        
        return cleaned_data

class UsersForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'groups']