from django.urls import path
from . import views
from .views import admin_login_view, admin_dashboard_view, admin_logout_view

urlpatterns = [
    path('', views.index, name='index'),
    path('subir/', views.subir_producto, name='subir_producto'),
    path('modificar/<int:pk>/', views.modificar_producto, name='modificar_producto'),
    path('eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    path('productos/casero/', views.productos_caseros, name='productos_caseros'),
    path('productos/maceteros/', views.productos_maceteros, name='productos_maceteros'),
    path('productos/thojas/', views.productos_thojas, name='productos_thojas'),
    path('productos/todos/', views.productos_totales, name='todo_prod'),
    path('registro/', views.registro_user, name='registro'),
    path('phone_login/', views.phone_login_view, name='phone_login'),
    path('compra/', views.compra, name='compra'),
    path('presentacion/', views.presentacion, name='presentacion'),
    path('contacto/', views.contacto, name='contacto'),
    path('ayuda/', views.ayuda, name='ayuda'),
    path('admin_login/', admin_login_view, name='admin_login'),
    path('admin_dashboard/', admin_dashboard_view, name='admin_dashboard'),
    path('admin_logout/', admin_logout_view, name='admin_logout'),
    path('logout/', views.logout_view, name='logout'),

]
