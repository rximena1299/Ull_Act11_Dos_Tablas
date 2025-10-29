from django.urls import path
from . import views

app_name = 'app_producto'

urlpatterns = [
    # URLs para productos
    path('', views.listar_productos, name='listar_productos'),
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    path('productos/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('productos/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('productos/borrar/<int:producto_id>/', views.borrar_producto, name='borrar_producto'),
    
    # URLs para categorías
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('categorias/crear/', views.crear_categoria, name='crear_categoria'),
    path('categorias/crear/<int:producto_id>/', views.crear_categoria_producto, name='crear_categoria_producto'),
    path('categorias/<int:categoria_id>/', views.detalle_categoria, name='detalle_categoria'),
    path('categorias/editar/<int:categoria_id>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/borrar/<int:categoria_id>/', views.borrar_categoria, name='borrar_categoria'),
]