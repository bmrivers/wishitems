from django.shortcuts import render

# Add the following import
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import requests
from .models import Item

# Define the home view
def home(request):
    items_list = Item.objects.all()
    return render(request, 'index.html', {'items_list': items_list})

class ItemCreate(CreateView):
    model = Item
    fields = '__all__'
    success_url = '/'