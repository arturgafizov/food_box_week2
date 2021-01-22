from items.views import Itemlist, Itemretrieve
from django.urls import path

urlpatterns_items = [
    path('items/', Itemlist.as_view(), name='Itemlist'),
    path('items/<int:pk>/', Itemretrieve.as_view(), name='Itemretrieve'),
]
