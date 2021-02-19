from django.shortcuts import render
# !import the model
from .models import Hospital


# Create your views here.
# ! write a django view (function based) to pull all data from hospital table

def getHospitals(request):
    # !write model query here -- get the data from the model
    all_hospitals = Hospital.objects.all()  # ! select * from hospital_hospital
    return render(request, 'hospitals.html', {'all_hospitals_key': all_hospitals})
