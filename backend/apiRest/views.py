from django.shortcuts import render

from django.shortcuts import redirect, render
from django.http import HttpResponse
import random
from .models import Producto,Categorias,pyme
from .serializers import pymeSerializer,productoSerializer,categoriaSerializer
from rest_framework import generics



class listarProducto(generics.ListAPIView):
    queryset =Producto.objects.all()
    serializer_class = productoSerializer


class crarProducto(generics.ListCreateAPIView):
    
    queryset =Producto.objects.all()
    serializer_class = productoSerializer



class modificarProducto(generics.RetrieveUpdateDestroyAPIView):
    queryset =Producto.objects.all()
    serializer_class = productoSerializer


class eliminarProducto(generics.RetrieveDestroyAPIView):

    queryset =Producto.objects.all()
    serializer_class = productoSerializer

##################################################################################################################################################################################################


class listarPyme(generics.ListAPIView):

    queryset =pyme.objects.all()
    serializer_class = pymeSerializer


class crearPyme(generics.ListCreateAPIView):

    queryset =pyme.objects.all()
    serializer_class = pymeSerializer



class modificarPyme(generics.RetrieveUpdateDestroyAPIView):
    queryset =pyme.objects.all()
    serializer_class = pymeSerializer


class eliminarPyme(generics.RetrieveDestroyAPIView):

    queryset =pyme.objects.all()
    serializer_class = pymeSerializer


##################################################################################################################################################################################################


class listarCategoria(generics.ListAPIView):

    queryset =Categorias.objects.all()
    serializer_class = categoriaSerializer


class crearCategoria(generics.ListCreateAPIView):

    queryset =Categorias.objects.all()
    serializer_class = categoriaSerializer



class modificarCategoria(generics.RetrieveUpdateDestroyAPIView):
    queryset =Categorias.objects.all()
    serializer_class = categoriaSerializer


class eliminarCategoria(generics.RetrieveDestroyAPIView):

    queryset =Categorias.objects.all()
    serializer_class = categoriaSerializer

