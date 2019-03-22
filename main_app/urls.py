from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.ItemCreate.as_view(), name="item_create")
]