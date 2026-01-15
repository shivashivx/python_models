from django.shortcuts import render,redirect
from django.http import HttpResponse
from doctors.models import Doctor
from departments.models import Department

# Create your views here.

def addDoctor(request):
    if request.method=="POST":
        d_name=request.POST["name"]
        dep=request.POST["department"]
        dob=request.POST["dob"]
        gender=request.POST["gender"]
        j_date=request.POST["join_date"]
        s=request.POST["salary"]
        q=request.POST["qualification"]
        about=request.POST["about"]
        pic=request.FILES.get("image")
        dep_instance=Department.objects.get(id=dep)
        if pic :
            Doctor(name=d_name,department=dep_instance,
               dob=dob,gender=gender,salary=s,
               join_date=j_date,
               qualification=q,about=about,
               image=pic).save()
        else:
            Doctor(name=d_name,department=dep_instance,
               dob=dob,gender=gender,salary=s,
               join_date=j_date,
               qualification=q,about=about).save()
        return HttpResponse("New Doctor added")
    dep=Department.objects.all()
    return render(request,"doctors/add-doctors.html",{"departments":dep})

def viewDoctor(request):
    drs=Doctor.objects.all()
    return render(request,"doctors/list_doctor.html",{"doctors":drs})

def editDoctor(request,de_id):
    dr=Doctor.objects.get(id=de_id)
    if request.method=="POST":
        d_name=request.POST["name"]
        dep=request.POST["department"]
        dob=request.POST["dob"]
        gender=request.POST["gender"]
        j_date=request.POST["join_date"]
        s=request.POST["salary"]
        q=request.POST["qualification"]
        about=request.POST["about"]
        pic=request.FILES.get("image",None)
        dep_instance=Department.objects.get(id=dep)

        data={"name":d_name,"department":dep_instance,
               "dob":dob,"gender":gender,
               "join_date":j_date,"salary":s,
               "qualification":q,"about":about}
        
        if pic is not None:
            data["image"]=pic
        
        Doctor(**data).save()
    
        return HttpResponse("New Doctor added")
    dep=Department.objects.all()
    return render(request,"doctors/add-doctor.html",{"departments":dep})

def viewDoctors(request):
    drs=Doctor.objects.all()
    return render(request,"doctors/list-doctors.html",{"doctors":drs})

def editDoctor(request,dr_id):
    dr=Doctor.objects.get(id=dr_id)
    if request.method=="POST":
        d_name=request.POST["name"]
        dep=request.POST["department"]
        dob=request.POST["dob"]
        gender=request.POST["gender"]
        j_date=request.POST["join_date"]
        s=request.POST["salary"]
        q=request.POST["qualification"]
        about=request.POST["about"]
        pic=request.FILES.get("image",None)
        dep_instance=Department.objects.get(id=dep)
        dr.name=d_name
        dr.department=dep_instance
        dr.dob=dob
        dr.gender=gender
        dr.join_date=j_date
        dr.qualification=q
        dr.salary=s
        dr.about=about
        if pic:
            dr.image=pic
        dr.save()
        return redirect("doctors:list_doctor")
     
    dep=Department.objects.all()
    return render(request,"doctors/edit-doctor.html",{"doctor":dr,"departments":dep})

