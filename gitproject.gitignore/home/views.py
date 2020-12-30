from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import contact
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from home.froms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Account created has been created {username}')
            return redirect('/login')
    else:
        form = UserRegisterForm()
    return render(request,'register.html',{'form':form})
    

# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def travel(request):
    if request.method=="POST":  
        print("this is Post")
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        print(name,email,phone)
        ins=contact(name=name,email=email,phone=phone,date=datetime.today())
        ins.save()
        print("we done it")
    return render(request,"travel.html")
def food(request):
    return render(request,"food.html")
 