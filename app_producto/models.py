from django.db import models

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    stock_actual = models.IntegerField()
    fecha_vencimiento = models.DateField()
    foto_producto = models.ImageField(upload_to='productos_img/', blank=True, null=True)

    def __str__(self):
        return self.nombre_producto

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    contenido = models.TextField()
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='categorias')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"