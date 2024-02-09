from django.shortcuts import render
from .models import Department, Drink


# Create your views here.

def index(request):
    departments = Drink.objects.all()
    return render(request, 'home/index.html', {'departments': departments})

