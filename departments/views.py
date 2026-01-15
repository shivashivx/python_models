from django.shortcuts import render
from departments.models import Department
from django.http import HttpResponse
# Create your views here.
def addDepartment(request):
    if request.method=="POST":
        depart=request.POST['dep']
        desc=request.POST["description"]
        Department(name=depart,description=desc).save()
        return HttpResponse("new department added")
    return render(request,"departments/add-department.html")

def AllDepartments(request):
    dep=Department.objects.all()
    return render(request,"departments/all-department.html",{"departments":dep})