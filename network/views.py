from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets

from network.models import NetworkObject, Product
from network.serializers import ObjectSerializer, ObjectUpdateSerializer, ProductSerializer
from users.permissions import IsActiveUser


class ObjectCreateAPIView(generics.CreateAPIView):
    """ Контроллер для создания объекта сети """
    serializer_class = ObjectSerializer
    permission_classes = [IsActiveUser]


class ObjectListAPIView(generics.ListAPIView):
    """ Контроллер для просмотра списка объектов сети """
    serializer_class = ObjectSerializer
    queryset = NetworkObject.objects.all()
    permission_classes = [IsActiveUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']


class ObjectRetrieveAPIView(generics.RetrieveAPIView):
    """ Контроллер для просмотра объекта сети """
    serializer_class = ObjectSerializer
    queryset = NetworkObject.objects.all()
    permission_classes = [IsActiveUser]


class ObjectUpdateAPIView(generics.UpdateAPIView):
    """ Контроллер для изменения объекта сети """
    serializer_class = ObjectUpdateSerializer
    queryset = NetworkObject.objects.all()
    permission_classes = [IsActiveUser]


class ObjectDestroyAPIView(generics.DestroyAPIView):
    """ Контроллер для удаления объекта сети """
    queryset = NetworkObject.objects.all()
    permission_classes = [IsActiveUser]


class ProductViewSet(viewsets.ModelViewSet):
    """ Контроллер для управления моделью Продукты """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveUser]
