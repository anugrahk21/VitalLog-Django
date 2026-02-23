from django.shortcuts import render, redirect
from app.forms import PatientForm, UsersForm
from app.models import Patient
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
#import groups,permissions
from django.contrib.auth.models import Group, Permission

@login_required(login_url='login')
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST) # Takes what the user typed and puts it back into the memory object.
        if form.is_valid(): # Checks if the data is valid
            form.save() # Takes the data from memory and writes a row in your database auth_user table.
            return redirect('add_patient') # Redirect to home/add_patient on success
        else:
            print("Form is invalid. Errors:", form.errors)
    else:
        form = PatientForm() # Creates a blank form in memory.
    
    # Renders the add_patient.html template and passes the form object to it.
    # The form object is passed to the template in a dictionary with the key 'form'.
    # This allows the template to access the form object using {{ form }}.
    # The 'form' variable in the template is used to display the form fields -> {{form.as_p}}
    return render(request, 'add_patient.html', {'form': form})

def add_user(request):
    if request.method == 'POST':
        form = UsersForm(request.POST) # Takes the raw data from the form
        if form.is_valid(): # Checks if the data is valid
            form.save() # Takes the data from memory and writes a row in your database auth_user table.
            return redirect('login')  # Redirect to login after adding the user
        else:
            print("Form is invalid. Errors:", form.errors)
    else:
        form = UsersForm() # Makes a empty form to be filled by the user, this is shown on html page using {{form.as_p}}
    
    return render(request, 'add_user.html', {'form': form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('add_patient') # Redirect to home/add_patient on success
        else:
            print("Form is invalid. Errors:", form.errors)
    else:
        form = AuthenticationForm() # Built-in Django form for authentication
    
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    patients = Patient.objects.all()
    return render(request, 'view.html', {'patients': patients})