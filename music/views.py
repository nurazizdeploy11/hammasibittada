from django.shortcuts import render
from .models import *
from django.db.models import Q
# Create your views here.
def home(request):
     if 'q' in request.GET:
        category = Category.objects.all()
        qidiruvdagi_soz = request.GET.get('q')
        author = Author.objects.all()
        music = Music.objects.filter(Q(title__icontains=qidiruvdagi_soz))
     else:
        music = Music.objects.all()
        category = Category.objects.all()
        author = Author.objects.all()
     con={
        'music':music,
        'category':category,
        'author':author,
     }   
     return render(request,'music.html',con)
def categores(request):
    qi = request.GET.get('category')
    category = Category.objects.all()
    if category == None:
        music = Music.objects.all()
    else:
        music = Music.objects.filter(category__name=qi)
    cont = {
        'category':category,
        'music':music,
    }
    return render(request,'musiccate.html',cont)