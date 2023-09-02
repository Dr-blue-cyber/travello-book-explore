from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def login(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']

        user = auth.authenticate(username=username, password = password) 
        if user is not None:
            auth.login(req, user)
            return redirect('/')
            
        else:
            messages.info(req, 'invalid credential')
            return redirect('login')
    else:
        return render(req, 'login.html')


def register(req):
    if req.method == "POST":
        firstname = req.POST['firstname']
        lastname = req.POST['lastname']
        email = req.POST['email']
        username = req.POST['username']
        password1 = req.POST['password1']
        password2 = req.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(req, "User name is Already Exists....")
                return redirect('register')
                
            elif User.objects.filter(email= email).exists():
                messages.info(req, "Eamil id is Already Exists....")
                return redirect('register')
                
            else:
                user = User.objects.create_user(first_name= firstname, last_name = lastname, email=email, username= username,password=password1)
                user.save()
                print('User Created...') 
                return redirect('login')
        else:
            print('password not mathching.........')
            return redirect('register')
        
    else:
        return render(req, 'register.html')
    
def logout(req):
    auth.logout(req) 
    return redirect('/')