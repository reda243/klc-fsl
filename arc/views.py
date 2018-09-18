from . import models
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import forms
from arc.forms import SignUpForm
from arc.forms import Reservation
from arc.forms import Log
from arc.forms import Voit
from arc.forms import Serv
from .models import voitures
from .models import logements
#from .models import logementt
from .models import services
from .models import res

# Create your views here.

@login_required
def home(request):
    return render(request, 'home.html')


def res(request):
    return render(request, 'res.html')


def index(request):
    return render (request, 'index.html')


def book(request):
    return render (request, 'book.html')





def logement(request):
    posts= logements.objects.all()
    return render (request, 'logement.html', {'logements': posts})



def voiture(request):
    posts1= voitures.objects.all()
    return render (request, 'vehicule.html', {'voitures': posts1})



def service(request):
    posts2= services.objects.all()
    return render (request, 'service.html', {'services': posts2})





#def res(request):
 #   posts3= res.objects.all()
  #  return render (request, 'res.html', {'res': posts3}) 

#def log(request):
 #   posts4= log.objects.all()
  #  return render (request, 'res.html', {'res': posts4})  




def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



def reservation(request):
    if request.method == 'POST':
        form = Reservation(request.POST)
        if form.is_valid():
            form.save()
            Nom = form.cleaned_data.get('Nom') 
            return render(request, 'res.html')
    else:
        form = Reservation()
    return render(request, 'reservation.html', {'form': form})



def log(request):
    if request.method == 'POST':
        form = Log(request.POST)
        if form.is_valid():
            form.save()
            Nom = form.cleaned_data.get('Nom') 
            return render(request, 'loge.html')
    else:
        form = Log()
    return render(request, 'log.html', {'form': form})


def serv(request):
    if request.method == 'POST':
        form = Serv(request.POST)
        if form.is_valid():
            form.save()
            Nom = form.cleaned_data.get('Nom') 
            return render(request, 'serve.html')
    else:
        form = Serv()
    return render(request, 'serv.html', {'form': form})



def voit(request):
    if request.method == 'POST':
        form = Voit(request.POST)
        if form.is_valid():
            form.save()
            Nom = form.cleaned_data.get('Nom') 
            return render(request, 'voite.html')
    else:
        form = Voit()
    return render(request, 'voit.html', {'form': form})













