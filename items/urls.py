from rest_framework.routers import DefaultRouter

from items.views import ItemViewset
from items.views import item_detail
from django.urls import path
#router = DefaultRouter()
#router.register('items', ItemViewset, basename='item')
#urlpatterns_item = router.urls




urlpatterns_items = [
    path('items/<int:pk>/', item_detail, name='item_detail'),
]
