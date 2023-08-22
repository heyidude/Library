from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login as auth_login
from.models import Books

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')

def login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Using the correct login function
            return redirect('loginpage')
        else:
            return redirect('signup')
        
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        myuser = User.objects.create_user(username, email, password)
        myuser.save()
        return redirect('login')

        
    return render(request, 'signup.html')

def books(request):
    dict_boo ={
        'books': Books.objects.all()
    }
    return render(request, 'books.html' , dict_boo)

def loginpage(request):
    return render(request, 'loginpage.html')
def buy(request):
    return render(request,'buy.html')
