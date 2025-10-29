from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria
from .forms import ProductoForm, CategoriaForm

# Vistas para Producto
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id_producto=producto_id)
    return render(request, 'detalle_producto.html', {'producto': producto})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app_producto:listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'formulario_producto.html', {'form': form, 'titulo': 'Crear Producto'})

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id_producto=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('app_producto:detalle_producto', producto_id=producto.id_producto)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'formulario_producto.html', {'form': form, 'titulo': 'Editar Producto'})

def borrar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id_producto=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('app_producto:listar_productos')
    return render(request, 'confirmar_borrar_producto.html', {'producto': producto})

# Vistas para Categoria
def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'listar_categorias.html', {'categorias': categorias})

def detalle_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id_categoria=categoria_id)
    return render(request, 'detalle_categoria.html', {'categoria': categoria})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_producto:listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'formulario_categoria.html', {'form': form, 'titulo': 'Crear Categoría'})

def crear_categoria_producto(request, producto_id):
    producto = get_object_or_404(Producto, id_producto=producto_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.id_producto = producto
            categoria.save()
            return redirect('app_producto:detalle_producto', producto_id=producto_id)
    else:
        form = CategoriaForm(initial={'id_producto': producto})
    return render(request, 'formulario_categoria.html', {
        'form': form, 
        'titulo': f'Crear Categoría para {producto.nombre_producto}',
        'producto': producto
    })

def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id_categoria=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('app_producto:detalle_categoria', categoria_id=categoria.id_categoria)
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'formulario_categoria.html', {
        'form': form, 
        'titulo': 'Editar Categoría'
    })

def borrar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id_categoria=categoria_id)
    producto_id = categoria.id_producto.id_producto
    if request.method == 'POST':
        categoria.delete()
        return redirect('app_producto:detalle_producto', producto_id=producto_id)
    return render(request, 'confirmar_borrar_categoria.html', {'categoria': categoria})