from django.urls import path
from . import views


app_name="patient"

urlpatterns=[
    path("add-patient",views.add_patient,name="new_patient")
]