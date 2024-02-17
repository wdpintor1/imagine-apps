from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from .models import Paquete
from django.core.paginator import Paginator, EmptyPage
from django.views.generic import CreateView
from .forms import PaqueteForm
from django.contrib import messages

def home(request):    
    return render(request, 'home.html')

