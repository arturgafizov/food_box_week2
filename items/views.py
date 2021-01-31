from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from items.models import Item
from items.models import ItemSerializer


@api_view(http_method_names=['GET'])
def get_item_view(request, pk):
    item = Item.objects.get(id=pk)

    return Response({
        'id': item.id,
        'title': item.title,
        'description': item.description,
        'weight': item.weight,
        'price': item.price,
    })


class ItemList(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
