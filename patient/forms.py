from django import forms
from patient.models import patient

class patientForm(forms.ModelForm):
    class Meta:
        model=patient
        fields=["patient_code",
                "name",
                "dob",
                'gender',
                'phone',
                'address',
                ]