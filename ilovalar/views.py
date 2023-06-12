from django.shortcuts import render
from .models import *
from django.db.models import Q
# Create your views here.
def home(request):
     if 'q' in request.GET:
        category = Category.objects.all()
        qidiruvdagi_soz = request.GET.get('q')
        author = Author.objects.all()
        ilova = Ilova.objects.filter(Q(title__icontains=qidiruvdagi_soz))
     else:
        ilova = Ilova.objects.all()
        category = Category.objects.all()
        author = Author.objects.all()
     con={
        'ilova':ilova,
        'category':category,
        'author':author,
     }   
     return render(request,'ilova.html',con)
def categores(request):
    qi = request.GET.get('category')
    category = Category.objects.all()
    if category == None:
        ilova = Ilova.objects.all()
    else:
        ilova = Ilova.objects.filter(category__name=qi)
    cont = {
        'category':category,
        'ilova':ilova,
    }
    return render(request,'ilovacate.html',cont)