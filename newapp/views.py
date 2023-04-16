from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm



def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request,'dashboard.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form':form})


def transportationlink(request):
    return render(request, 'transportationlink.html')


def transportation(request):
    return render(request, 'transportation.html')

def donate(request):
    return render(request,'donate.html')

