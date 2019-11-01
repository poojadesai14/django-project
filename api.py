from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .serializers import ListSerializer, CardSerializer

from scrumboard.models import List, Card


class ListViewSet(ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (permissions.IsAuthenticated,)
