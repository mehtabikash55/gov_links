from ast import Param
from multiprocessing import context
from turtle import title
from django.shortcuts import render, HttpResponse
from link import models
from link.models import home_page, province, metropolitan, sub_metropolitan, municipality, rural_municipality, Social_Media_db, gov_form

# Create your views here.
def home(request):
    if 'query' in request.GET:
        query = request.GET['query']
        data = home_page.objects.filter(Website_Title__icontains = query)
    else:
        data = home_page.objects.all()
    context = {'metro' : data}
    # return HttpResponse("This is home")
    return render(request, 'index.html', context)
    
    
def gov_forms(request):
    if 'query' in request.GET:
        query = request.GET['query']
        data = gov_form.objects.filter(Website_Title__icontains = query)
    else:
        data = gov_form.objects.all()
    context = {'metro' : data}
    return render(request, 'gov_form.html', context)

def provinces(request):
    if 'query' in request.GET:
        query = request.GET['query']
        data = province.objects.filter(Website_Title__icontains = query)
    else:
        data = province.objects.all()
    context = {'metro' : data}
    return render(request, 'province.html', context)

def metropolitans(request):
    if 'query' in request.GET:
        query = request.GET['query']
        data = metropolitan.objects.filter(Website_Title__icontains = query)
    else:
        data = metropolitan.objects.all()
    context = {'metro' : data}
    return render(request, 'metropolitan.html', context)

def sub_metropolitans(request):
    if 'query' in request.GET:
        query = request.GET['query']
        data = sub_metropolitan.objects.filter(Website_Title__icontains = query)
    else:
        data = sub_metropolitan.objects.all()
    context = {'metro' : data}
    return render(request, 'sub_metropolitan.html', context)

def municipalities(request):
    if 'query' in request.GET:
        query = request.GET['query']
        data = municipality.objects.filter(Website_Title__icontains = query)
    else:
        data = municipality.objects.all()
    context = {'metro' : data}
    return render(request, 'municipality.html', context)

def rural_municipalities(request):
    if 'query' in request.GET:
        query = request.GET['query']
        data = rural_municipality.objects.filter(Website_Title__icontains = query)
    else:
        data = rural_municipality.objects.all()
    context = {'metro' : data}
    return render(request, 'rural_municipality.html', context)

def Social_Media(request):
    if 'query' in request.GET:
        query = request.GET['query']
        data = Social_Media_db.objects.filter(Website_Title__icontains = query)
    else:
        data = Social_Media_db.objects.all()
    context = {'metro' : data}
    return render(request, 'Social_Media.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        dics = request.POST['dics']
        print(name, email, phone, dics)
        ins = models.contact(Name=name, Email_Id=email, Phone_Number=phone, Message=dics)
        ins.save()
        print("Data entered")
    # return HttpResponse("This is home")
    return render(request, 'contact.html') 
