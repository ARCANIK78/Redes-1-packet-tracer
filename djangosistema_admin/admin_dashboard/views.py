from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseForbidden,JsonResponse
import requests

def dashboard_view(request):
    # Obtén los productos desde la API (ajusta la URL según sea necesario)
    response = requests.get('http://localhost:8000/api/productos/')
    
    if response.status_code == 200:
        productos = response.json()  # Obtén los productos de la API
    else:
        productos = []  # Si no hay productos, pasa una lista vacía
    
    return render(request, 'admin_dashboard/dashboard.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        # Realiza la solicitud POST a la API para crear un producto
        response = requests.post('http://localhost:8000/api/productos/', data={'nombre': nombre, 'precio': precio})
        if response.status_code == 201:
            return redirect('dashboard')  # Redirige al dashboard después de crear el producto
        else:
            return HttpResponse('Error al crear producto', status=400)
    return render(request, 'admin_dashboard/crear_producto.html')

def editar_producto(request, id):
    # Obtén el producto a editar desde la API
    response = requests.get(f'http://localhost:8000/api/productos/{id}/')
    print(response.status_code)  # Imprime el código de estado para ver si es correcto
    if response.status_code != 200:
        return HttpResponse('Producto no encontrado', status=404)

    producto = response.json()

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        # Realiza la solicitud PUT a la API para editar el producto
        response = requests.put(f'http://localhost:8000/api/productos/{id}/', data={'nombre': nombre, 'precio': precio})
        print(response.status_code)  # Imprime el código de estado para ver si la modificación fue exitosa
        if response.status_code == 200:
            return redirect('dashboard')  # Redirige al dashboard después de editar
        else:
            return HttpResponse('Error al editar producto', status=400)

    return render(request, 'admin_dashboard/editar_producto.html', {'producto': producto})

def eliminar_producto(request, id):
    if request.method == 'DELETE':
        # URL de tu API externa
        api_url = f'http://localhost:8000/api/productos/{id}/'

        # Realizamos la solicitud DELETE
        response = requests.delete(api_url)

        # Analizamos la respuesta de la API
        if response.status_code == 204:  # 204 No Content = éxito
            return JsonResponse({'message': 'Producto eliminado exitosamente'}, status=200)
        elif response.status_code == 404:  # 404 Not Found
            return JsonResponse({'error': 'Producto no encontrado en la API externa'}, status=404)
        else:
            return JsonResponse({'error': f'Error al eliminar el producto: {response.status_code}'}, status=500)

    # Si no es DELETE, devolvemos un error 405 (Método no permitido)
    return HttpResponse('Método no permitido', status=405)