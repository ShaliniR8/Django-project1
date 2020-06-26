from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .form import ProductForm, SearchForm
from decimal import *

# Create your views here.


def search(request):
     print("Inside search")
     if request.method == 'GET':
          if not request.GET:
               pass
               #print("GET METHOD NOT BY FORM: ", request.GET)
          else:
               #print("GET METHOD BY FORM: ", request.GET)
               route = request.GET['search']
               return redirect('../search/'+route+'/')
     

     return render(request, 'search.html')


def individual_view(request, i):

     #print("Inside lookup")
     if request.method == 'GET':
          if not request.GET:
               pass
               #print("GET METHOD NOT BY FORM: ", request.GET)
          else:
               #print("GET METHOD BY FORM: ", request.GET)
               route = request.GET['search']
               return redirect('../../search/'+route+'/')


     if request.method == 'POST':
          obj = Product.objects.get(id = i)
          #print("update")
          obj.ratings += Decimal(1)
          obj.save()

     obj = get_object_or_404(Product, id=i)
     
     dic={
          'obj': obj
     }
     return render(request, 'lookup.html', dic)

def home_view(request):
     #print("request meta:",request.META.get('PATH_INFO', None))
     querySet = Product.objects.all().order_by('-ratings')
     dic = {
          'objects' : querySet
     }
     return render (request, 'home.html', dic)


def form_view(request):
     if request.method == 'POST':
          #print("post")
          obj = ProductForm(request.POST)
          if obj.is_valid():
               print('is valid')
               cleaned = obj.cleaned_data
               Product.objects.create(**cleaned)
          # else:
          # print('Not valid')
     else:
          obj = ProductForm()
          #print("get")
     instance = {
          'obj' : obj
     }
     return render (request, 'form.html', instance)


def about_view(request):
     
     instance = {}
     return render (request, 'about.html', instance)

def empty_view(request):

     return render (request, 'base.html')