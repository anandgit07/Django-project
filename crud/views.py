from django.shortcuts import render,redirect
from crud.models import student

# Create your views here.
def home(request):
    std=student.objects.all()
    return   render(request,"crud/home.html",{'std':std})


def std_add(request):
    if request.method=="POST":
          print("Added")
          roll=request.POST.get("roll")  
          name=request.POST.get("name")  
          email=request.POST.get("email")  
          address=request.POST.get("address")  
          phone=request.POST.get("phone")  
          #create aobject from model class
          s=student(roll=roll,name=name,email=email,address=address,phone=phone)
          s.save()
           
          return redirect("/crud/home")


    return render (request,"crud/std.html")


def delete_std(request,roll):
     s=student.objects.get(pk=roll)
     s.delete()
     return redirect("/crud/home")

def update_std(request,roll):
     std=student.objects.get(pk=roll)
     
     return render(request,"crud/update.html",{'std':std})

def edit(request,id):
        
         if request.method == "POST":
           name=request.POST.get('name')
           roll=request.POST.get('roll')
           email=request.POST.get('email')
           address=request.POST.get('address')
           phone=request.POST.get('phone')
            
           std= student(id=id,name=name,roll=roll,email=email,address=address,phone=phone) 
           std.save()
           return redirect("home")
         return render(request,"crud/update.html") 
            
          
   