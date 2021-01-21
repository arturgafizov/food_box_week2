from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
import requests
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from items.models import Item
from items.models import ItemSerializer
# Create your views here.
@api_view(http_method_names=['GET'])
def item_detail(request, pk):
    link_item = requests.get('https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/foodboxes.json')
    items = link_item.json()
    d = {}
    response = None

    for item in items:
        if item['id'] == pk:
            d['id'] = item['id']
            d['title'] = item['title']
            d['description'] = item['description']
            d['image'] = item['image']
            d['weight'] = item['weight_grams']
            d['price'] = item['price']
            response = d

    if response:
        return Response(response)
    elif link_item.status_code == 404:
        return Response(status=status.HTTP_404_NOT_FOUND)
    elif link_item.status_code == 408:
        return Response(status=status.HTTP_408_REQUEST_TIMEOUT)


class ItemViewset(ViewSet):
    def list(self, request):
        queryset = Item.objects.all()
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Item.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)
