from django import forms
from .models import Producto, Categoria

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre_producto', 'categoria', 'precio_unitario', 'stock_actual', 'fecha_vencimiento', 'foto_producto']
        widgets = {
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date'}),
            'nombre_producto': forms.TextInput(attrs={'placeholder': 'Nombre del producto'}),
            'categoria': forms.TextInput(attrs={'placeholder': 'Categoría del producto'}),
            'precio_unitario': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
            'stock_actual': forms.NumberInput(attrs={'min': '0'}),
        }
        labels = {
            'precio_unitario': 'Precio Unitario ($)',
            'stock_actual': 'Stock Actual'
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion', 'contenido', 'id_producto']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Descripción breve de la categoría'}),
            'contenido': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Contenido detallado de la categoría'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre de la categoría'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_producto'].label = "Producto"