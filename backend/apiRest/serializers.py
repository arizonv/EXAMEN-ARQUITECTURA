from dataclasses import fields
from django import forms
from .models import Producto,pyme,Categorias
from rest_framework import serializers


class productoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


class pymeSerializer (serializers.ModelSerializer):
    class Meta:
        model = pyme
        fields = '__all__'

class categoriaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'


