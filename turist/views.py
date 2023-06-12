from django.shortcuts import render
from .models import *
from django.db.models import Q
# Create your views here.
def home(request):
     if 'q' in request.GET:
        qidiruvdagi_soz = request.GET.get('q')
        manzil = Manzil.objects.filter(Q(title__icontains=qidiruvdagi_soz))
     else:
        manzil = Manzil.objects.all()
     con={
        'manzil':manzil,
     }   
     return render(request,'turs.html',con)