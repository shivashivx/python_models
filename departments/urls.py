from django.urls import path
from departments import views

app_name="departments"

urlpatterns=[
    path("add-department",views.addDepartment ,name="add_dep"),
    path("all-department",views.AllDepartments,name="list_dep")
]