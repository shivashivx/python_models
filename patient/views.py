from django.shortcuts import render
from patient.forms import patientForm
from django.http import HttpResponse
# Create your views here.
def add_patient(request):
    if request.method=="POST":
        p_form=patientForm(request.POST)
        if p_form.is_valid():
            p_form.save()
            return HttpResponse("new patient added")
    else:
            p_form=patientForm()
            return render(request,"patient/add_patient.html",{"pf_form":p_form})
