from django.shortcuts import render, redirect
from app.forms import PatientForm
from app.models import Patient
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

