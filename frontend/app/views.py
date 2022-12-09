import json
import random
import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.forms import PasswordInput
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from pyexpat.errors import messages
from rest_framework import status
from .forms import CreateUserForm,clientUserForm
from django.contrib.auth.decorators import login_required


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				return redirect('login')
		context = {'form':form}
		return render(request, 'log/register.html', context)

def registerClient(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = clientUserForm()
		if request.method == 'POST':
			form = clientUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				return redirect('login')
		context = {'form':form}
		return render(request, 'logClient/register.html', context)

def loginClient(request):
	if request.user.is_authenticated:
		return redirect('carrito')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('carrito')
			else:
				return redirect(to='login')
		context = {}
		return render(request, 'logClient/login.html', context)



def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				return redirect(to='login')
		context = {}
		return render(request, 'log/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('loginClient')

@login_required(login_url='Admin')
def Get_List(request):
	urlProductos="http://127.0.0.1:8000/api/productos/"
	urlPymes = "http://127.0.0.1:8000/api/pymes/"
	responsePr = requests.get(urlProductos).json()
	responsePy = requests.get(urlPymes).json()
	datos= {
		'productos':responsePr,
		'pymes': responsePy
	}
	return render(request, 'home.html', datos)

@login_required(login_url='Admin')
def eliminarProducto(request, id):
    url = f'http://127.0.0.1:8000/api/producto/{id}/'
    response = requests.delete(url)
    return redirect(to="home")

@login_required(login_url='Admin')
def eliminarPyme(request, id):
    url = f'http://127.0.0.1:8000/api/pyme/{id}/'
    response = requests.delete(url)
    return redirect(to="home")

@login_required(login_url='Admin')
def agregar(request):
	url = 'http://127.0.0.1:8000/api/producto/'
	
	url_pymes= 'http://127.0.0.1:8000/api/pymes/'
	url_categorias = 'http://127.0.0.1:8000/api/categorias/'

	responsePymes = requests.get(url_pymes).json()
	responseCategorias = requests.get(url_categorias).json()
	datos = {
		'categorias': responseCategorias,
		'pymes': responsePymes
	}
	if request.method == 'POST':
		response = requests.post(url,data=request.POST).json()
		print(response)
		return redirect(to='home')


	return render(request, "controllers/productos/agregar.html",datos)

@login_required(login_url='Admin')
def modificar(request,id):   

	url_pymes= 'http://127.0.0.1:8000/api/pymes/'
	url_categorias = 'http://127.0.0.1:8000/api/categorias/'
	
	urlProductos = f'http://127.0.0.1:8000/api/productoUp/{id}/'

	responseProducto= requests.get(urlProductos).json()
	responsePymes = requests.get(url_pymes).json()
	responseCategorias = requests.get(url_categorias).json()
	
	developer = {
		'categorias': responseCategorias,
		'pymes': responsePymes,
        'dev' : responseProducto,
        }
	if request.method == 'POST':
		developer = requests.put(urlProductos,data=request.POST)
		developer ={
			'dev': developer
		}
		return redirect(to='home')
	return render(request, "controllers/productos/modificar.html", developer )

@login_required(login_url='Admin')
def modificarPyme(request,id):   
	url_pymes= f'http://127.0.0.1:8000/api/pymeUp/{id}/'
	responsePymes = requests.get(url_pymes).json()
	
	developer = {
		'pymes': responsePymes,
        }
	if request.method == 'POST':
		developer = requests.put(urlProductos,data=request.POST)
		developer ={
			'pymes': developer
		}
		return redirect(to='home')
	return render(request, "controllers/pymes/modificar.html", developer )

#########################################################################################################################################################################################################################

def Get_List_inv(request):
	urlProductos="http://127.0.0.1:8000/api/productos/"
	urlPymes = "http://127.0.0.1:8000/api/pymes/"
	responsePr = requests.get(urlProductos).json()
	responsePy = requests.get(urlPymes).json()
	datos= {
		'productos':responsePr,
		'pymes': responsePy
	}
	return render(request, 'invitado.html', datos)

def delete(request):
	return render(request, 'eliminarCuenta.html')

def index(request):
	return render(request, 'index.html')


@login_required(login_url='Admin')
def user_delete(request, id):
    user = User.objects.get(id=id)
    if request.user == user:
        logout(request)
        user.delete()
        return redirect("home")
    else:
       messages.success(request, '"No tiene permiso para eliminar una operación".')


##################################################################################################################################################################################
	



@login_required(login_url='loginClient')
def Get_carrito(request):
	urlProductos="http://127.0.0.1:8000/api/productos/"
	urlPymes = "http://127.0.0.1:8000/api/pymes/"
	urlCate = "http://127.0.0.1:8000/api/categorias/"

	responsePr = requests.get(urlProductos).json()
	responsePy = requests.get(urlPymes).json()
	responseCa = requests.get(urlCate).json()
	datos= {
		'productos':responsePr,
		'pymes': responsePy,
		'categorias': responseCa
	}
	return render(request, 'usuario/carrito.html', datos)





