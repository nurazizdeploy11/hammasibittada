from django.shortcuts import render
from .models import *
from django.db.models import Q
# Create your views here.
def home(request):
     if 'q' in request.GET:
        category = Category.objects.all()
        qidiruvdagi_soz = request.GET.get('q')
        kitob = Kitob.objects.filter(Q(title__icontains=qidiruvdagi_soz))
     else:
        kitob = Kitob.objects.all()
        category = Category.objects.all()
     con={
        'kitob':kitob,
        'category':category,
     }   
     return render(request,'kitob.html',con)
def categores(request):
    qi = request.GET.get('category')
    category = Category.objects.all()
    if category == None:
        kitob = Kitob.objects.all()
    else:
        kitob = Kitob.objects.filter(category__name=qi)
    cont = {
        'category':category,
        'kitob':kitob,
    }
    return render(request,'kitobcate.html',cont)