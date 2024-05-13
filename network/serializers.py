from rest_framework import serializers

from network.models import NetworkObject, Product


class ObjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = NetworkObject
        fields = '__all__'


class ObjectUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = NetworkObject
        exclude = ['debt']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
