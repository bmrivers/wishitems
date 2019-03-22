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

def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)
    item.delete()
    success_url = '/'
    return home(request)

class ItemCreate(CreateView):
    model = Item
    fields = '__all__'
    success_url = '/'