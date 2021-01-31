from django.urls import path

from items.views import get_item_view, ItemList

urlpatterns_items = [
    path('<int:pk>/', get_item_view),
    path('', ItemList.as_view(), name='ItemList'),
]
