from django.shortcuts import render
from .models import *
from django.db.models import Q
# Create your views here.
def home(request):
     if 'q' in request.GET:
        category = Category.objects.all()
        qidiruvdagi_soz = request.GET.get('q')
        dars = Darslar.objects.filter(Q(nomi__icontains=qidiruvdagi_soz))
     else:
        dars = Darslar.objects.all()
        category = Category.objects.all()
     con={
        'dars':dars,
        'category':category,
     }   
     return render(request,'dars.html',con)
def categores(request):
    qi = request.GET.get('category')
    category = Category.objects.all()
    if category == None:
        dars = Darslar.objects.all()
    else:
        dars = Darslar.objects.filter(category__name=qi)
    cont = {
        'category':category,
        'dars':dars,
    }
    return render(request,'darscate.html',cont)