from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import ProductoForm, ProductoUpdateForm, RegistroForm, PhoneLoginForm
from .models import Productos, ControlUsuarios
from django.contrib.auth import logout

def get_context_with_welcome_message(request):
    context = {}
    if request.user.is_authenticated:
        context['mensaje_bienvenida'] = f'Hola, {request.user.username}!👋'
        context['usuario'] = request.user.username
    return context

def index(request):
    context = get_context_with_welcome_message(request)
    return render(request, 'index.html', context)

def presentacion(request):
    context = get_context_with_welcome_message(request)
    return render(request, 'presentacion.html', context)

def contacto(request):
    context = get_context_with_welcome_message(request)
    return render(request, 'contacto.html', context)

def ayuda(request):
    context = get_context_with_welcome_message(request)
    return render(request, 'ayuda.html', context)

def subir_producto(request):
    context = get_context_with_welcome_message(request)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('subir_producto')
    else:
        form = ProductoForm()
    context['form'] = form
    return render(request, 'formulario.html', context)

def modificar_producto(request, pk):
    context = get_context_with_welcome_message(request)
    producto = get_object_or_404(Productos, pk=pk)
    if request.method == 'POST':
        form = ProductoUpdateForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = ProductoUpdateForm(instance=producto)
    context['form'] = form
    return render(request, 'modificar_producto.html', context)

def eliminar_producto(request, id):
    context = get_context_with_welcome_message(request)
    producto = get_object_or_404(Productos, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('admin_dashboard')
    context['producto'] = producto
    return render(request, 'eliminar_producto.html', context)

def productos_caseros(request):
    context = get_context_with_welcome_message(request)
    productos_caseros = Productos.objects.filter(categoria='Casero')
    context['productos'] = productos_caseros
    return render(request, 'productos_caseros.html', context)

def productos_maceteros(request):
    context = get_context_with_welcome_message(request)
    productos_maceteros = Productos.objects.filter(categoria='Macetero')
    context['productos'] = productos_maceteros
    return render(request, 'productos_maceteros.html', context)

def productos_thojas(request):
    context = get_context_with_welcome_message(request)
    productos_thojas = Productos.objects.filter(categoria='thojas')
    context['productos'] = productos_thojas
    return render(request, 'productos_thojas.html', context)

def productos_totales(request):
    context = get_context_with_welcome_message(request)
    productos = Productos.objects.all()
    context['productos'] = productos
    return render(request, 'todo_prod.html', context)

def registro_user(request):
    context = get_context_with_welcome_message(request)
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegistroForm()
    context['form'] = form
    return render(request, 'registro.html', context)

def phone_login_view(request):
    context = get_context_with_welcome_message(request)
    if request.method == 'POST':
        form = PhoneLoginForm(request.POST)
        if form.is_valid():
            telefono = form.cleaned_data['telefono']
            try:
                user = ControlUsuarios.objects.get(telefono=telefono)
                login(request, user)
                return redirect('index')
            except ControlUsuarios.DoesNotExist:
                context['error_message'] = "Número de teléfono incorrecto."
    else:
        form = PhoneLoginForm()
    context['form'] = form
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('index')

def compra(request):
    context = get_context_with_welcome_message(request)
    products = request.GET.get('products', '').split(',')
    quantities = list(map(int, request.GET.get('quantities', '').split(',')))
    products_in_cart = []
    total = 0
    for product_name, quantity in zip(products, quantities):
        product = Productos.objects.get(nombre=product_name)
        products_in_cart.append((product, quantity))
        total += product.precio * quantity
    context['cart'] = products_in_cart
    context['total'] = total
    return render(request, 'compra.html', context)

def admin_login_view(request):
    context = get_context_with_welcome_message(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == 'admin' and password == 'admin':
            request.session['admin_logged_in'] = True
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid admin credentials')
    return render(request, 'admin_login.html', context)

def admin_dashboard_view(request):
    context = get_context_with_welcome_message(request)
    if not request.session.get('admin_logged_in'):
        return HttpResponseForbidden()
    productos = Productos.objects.all()
    context['productos'] = productos
    return render(request, 'admin_dashboard.html', context)

def admin_logout_view(request):
    request.session['admin_logged_in'] = False
    return redirect('admin_login')
