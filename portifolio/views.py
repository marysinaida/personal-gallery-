from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt



# Create your views here.
def welcome(request):
    return render(request,'welcome.html')
#function that display diffrent photo categories in cards.
def photo_category(request):
    date = dt.date.today()
    return render(request, 'all-Folio/category.html', {"date": date,})

def travel(request):
    date = dt.date.today()
    return render(request, 'all-Folio/travel.html', {"date": date,})

def party(request):
    date = dt.date.today()
    return render(request, 'all-Folio/party.html', {"date": date,})

def activity(request):
    date = dt.date.today()
    return render(request, 'all-Folio/activity.html', {"date": date,})
    
    

