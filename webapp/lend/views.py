from django.http import HttpResponse
from django.shortcuts import render
from .models import rent
from math import ceil
# Create your views here.
def index(request):
    rents = rent.objects.all()
    print(rents)
    n=len(rents)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params={'no_of_slides': nSlides,'range': range(1,nSlides) , 'rent': rents  }
    return render(request,'lend/index.html',params)
