from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.views.generic import DetailView
# Create your views here.
def home(request):
     if 'q' in request.GET:
        category = Category.objects.all()
        qidiruvdagi_soz = request.GET.get('q')
        film = Film.objects.filter(Q(nomi__icontains=qidiruvdagi_soz))
     else:
        film = Film.objects.all()
        category = Category.objects.all()
     con={
        'film':film,
        'category':category,
     }   
     return render(request,'tv.html',con)
def categores(request):
    qi = request.GET.get('category')
    category = Category.objects.all()
    if category == None:
        film = Film.objects.all()
    else:
        film = Film.objects.filter(category__name=qi)
    cont = {
        'category':category,
        'film':film,
    }
    return render(request,'cate.html',cont)
class detail(DetailView):
    model = Film
    template_name = 'detail.html'

