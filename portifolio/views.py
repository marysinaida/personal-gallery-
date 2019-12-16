from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from .models import *



# Create your views here.
def welcome(request):
    return render(request,'welcome.html')
#function that display diffrent photo categories in cards.
def photo_category(request):
    date = dt.date.today()
    portifolio = Image.objects.all
    return render(request, 'all-Folio/category.html', {"date": date, "portifolio":portifolio})

def search_results(request):
        if 'image' in request.GET and request.GET["image"]:
                search_term = request.GET.get("image")
                searched_images = Image.search_by_category(search_term)
                message = f"{search_term}"

                return render(request, 'all-Folio/search.html',{"message":message,"images":searched_images})

        else:
                message = "You havent searched for any term"
                return render(request,'all-Folio/search.html',{"message":message})

    
    

