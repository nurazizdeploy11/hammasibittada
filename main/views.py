from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def home(request):
    if request.method == 'POST':
        Contact.objects.create(
            name = request.POST['name'],
            tel = request.POST['tel'],
            text = request.POST['message']
        )
        return redirect('home')
    return render(request,'home.html')