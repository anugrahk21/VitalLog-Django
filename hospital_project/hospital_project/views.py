from django.shortcuts import render, redirect
from app.forms import PatientForm, UsersForm
from app.models import Patient
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

@login_required(login_url='login')
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_patient')
        else:
            print("Form is invalid. Errors:", form.errors)
    else:
        form = PatientForm()
    
    return render(request, 'add_patient.html', {'form': form})

def add_user(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after signing up
        else:
            print("Form is invalid. Errors:", form.errors)
    else:
        form = UsersForm()
    
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
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    patients = Patient.objects.all()
    return render(request, 'view.html', {'patients': patients})