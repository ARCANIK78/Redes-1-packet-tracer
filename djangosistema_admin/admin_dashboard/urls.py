from django.urls import path
from . import views



urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('producto/crear/', views.crear_producto, name='crear_producto'),
    path('producto/editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('producto/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    path('api/productos/<int:id>/', views.eliminar_producto, name='eliminar_producto'), 
]