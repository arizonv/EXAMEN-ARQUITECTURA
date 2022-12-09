import pickle
from django.contrib import admin
from django.urls import path
from .views  import  listarProducto,crarProducto,modificarProducto,eliminarProducto,listarPyme,crearPyme,modificarPyme,eliminarPyme,listarCategoria,crearCategoria,modificarCategoria,eliminarCategoria

urlpatterns = [

    path('api/productos/', listarProducto().as_view()),
    path('api/producto/', crarProducto().as_view()),
    path('api/productoUp/<pk>/', modificarProducto().as_view()),
    path('api/producto/<pk>/', eliminarProducto().as_view()),

    path('api/pymes/', listarPyme().as_view()),
    path('api/pyme/', crearPyme().as_view()),
    path('api/pymeUp/<pk>/', modificarPyme().as_view()),
    path('api/pyme/<pk>/', eliminarPyme().as_view()),

    path('api/categorias/', listarCategoria().as_view()),
    path('api/categoria/', crearCategoria().as_view()),
    path('api/categoriaUp/<pk>/', modificarCategoria().as_view()),
    path('api/categoria/<pk>/', eliminarCategoria().as_view()),
]
