from django.urls import path
from . import views


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('logAdmin/', views.loginPage, name="logAdmin"),  
	path('logout/', views.logoutUser, name="logout"),

    path('registerClient/', views.registerClient, name="registerClient"),
	path('loginClient/', views.loginClient, name="loginClient"),  


    path(r'', views.index , name='index' ),

    path('home', views.Get_List , name='home' ),
    path('invitado', views.Get_List_inv , name='invitado' ),

    path('delete', views.delete , name='delete' ),
    path('delete/<id>/', views.user_delete, name='delete'),


    path('eliminarProducto/<id>/', views.eliminarProducto , name='eliminarProducto' ),
    path('eliminarPyme/<id>/', views.eliminarPyme , name='eliminarPyme' ),

    path('modificar/<id>/', views.modificar , name='modificar' ),
    path('modificarPyme/<id>/', views.modificarPyme , name='modificarPyme' ),

    path('agregar/', views.agregar , name='agregar' ),

    path('carrito', views.Get_carrito , name='carrito' ),






]





