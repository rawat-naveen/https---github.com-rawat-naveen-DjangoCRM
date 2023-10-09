from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import Signupform
from .models import Record
from .forms import Addrecord
# Create your views here.

def home(request):
    records=Record.objects.all()
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You Have Loged in !!!")
            return redirect('home')
        else:
            messages.success(request,"Not found User !!")
            return redirect('home')
    else:
      return render(request,'home.html',{'records':records})
    
   
def logout_user(request):
    logout(request)
    messages.success(request,"You LOG OUT !!")
    return redirect('home')


def register_user(request):
    form=Signupform()
    if request.method =='POST':
        form=Signupform(request.POST)
        password1=request.POST['password1']
        password2=request.POST['password2']

        if form.is_valid():
            form.save()
            messages.success(request,"You Registered!!")
            return redirect('home')
        
        elif password1 !=password2:
            messages.success(request,"password and confirm password are not same !!")
            return redirect('register')
           
        else:
            messages.success(request,"You have not enter correct data for regisration")
            return redirect('register')
    
    else:
        form=Signupform()
        return render(request,'Register.html',{'form':form})

    
def record(request,id):
    if request.user.is_authenticated:
     customer_record=Record.objects.get(id=id)
     return render(request,'record.html',{'customer_record':customer_record})
    
    else:
        messages.success(request,"you must have to log in to see the record  ")
        return redirect('home')


def delete_record(request,id):
    if request.user.is_authenticated:
        delete_record=Record.objects.get(id=id)
        delete_record.delete()
        messages.success(request,"Record deleted successfully")
        return redirect('home')
    else:
            messages.success(request,"You must to login to delete record")
            return redirect('home') 

def add_record(request):
    form=Addrecord()
    if request.user.is_authenticated:
            if request.method =='POST':
                form=Addrecord(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request,"Record added successfully")
                    return redirect('home')
                return render(request,'add.html',{'form':form})
        
    else:
        messages.success(request,"You must to login to add record")
        return redirect('home')   
    
    return render(request,'add.html',{'form':form})


def update_record(request,id):
    if request.user.is_authenticated:
        current_record=Record.objects.get(id=id)
        form=Addrecord(request.POST or None ,instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"Record Updated Successfully !!!!")
            return redirect('home')
        return render(request,'update.html',{'form':form})
    
    else:
        messages.success(request,"You are not login ! please login ")
        return redirect('home')

        
