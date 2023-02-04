from django.db import models

# Create your models here.
    
class marca(models.Model):
    marca = models.CharField(max_length=40,verbose_name= "Nombre de la marca")
    create = models.DateField(auto_now_add= True,verbose_name= "Fecha de creacion")
    update = models.DateField(auto_now= True,verbose_name= "Fecha edicion")
    class Meta:
        verbose_name = "marca"
        verbose_name_plural = "marcas"
        ordering = ["-create"]
    def __str__(self):
            return self.marca


class talla(models.Model):
    talla = models.CharField(max_length= 3, verbose_name= "Talla")
    create = models.DateField(auto_now_add= True,verbose_name= "Fecha de creacion")
    update = models.DateField(auto_now= True,verbose_name= "Fecha edicion")
    class Meta:
        verbose_name = "talla"
        verbose_name_plural = "tallas"
        ordering = ["-create"]
    def __str__(self):
        return self.talla

class departamento(models.Model):
    nomDepartamento = models.CharField(max_length= 10, verbose_name= "Nombre del departamento")
    create = models.DateField(auto_now_add= True,verbose_name= "Fecha de creacion")
    update = models.DateField(auto_now= True,verbose_name= "Fecha edicion")
class Meta:
    verbose_name = "departamento"
    verbose_name_plural = "departamentos"
    ordering = ["-create"]
def __str__(self):
    return self.departamento

class proveedor(models.Model):
    nomProveedor = models.CharField(max_length= 15, verbose_name="Nombre del proveedor")
    telefono = models.CharField(max_length= 13, verbose_name="Numero de telefono")
    correo = models.TextField(verbose_name="e-mail")
    create = models.DateField(auto_now_add= True,verbose_name= "Fecha de creacion")
    update = models.DateField(auto_now= True,verbose_name= "Fecha edicion")
class Meta:
    verbose_name = "proveedor"
    verbose_name_plural = "proveedores"
    ordering = ["-create"]
def __str__(self):
    return self.proveedor

class cliente(models.Model):
    usuario = models.CharField(max_length=20, verbose_name="usuario")
    correo = models.TextField(verbose_name="e-mail")
    contraseña = models.CharField(max_length=8, verbose_name="contraseña")
    nomCliente = models.CharField(max_length = 40, verbose_name="Nombre del cliente")
    direccion = models.CharField(max_length= 100, verbose_name="Dirrecion")
    telefono = models.CharField(max_length=13, verbose_name="Numero de telefono")
    create = models.DateField(auto_now_add= True,verbose_name= "Fecha de creacion")
    update = models.DateField(auto_now= True,verbose_name= "Fecha edicion")
class Meta:
    verbose_name = "cliente"
    verbose_name_plural = "clientes"
    ordering = ["-create"]
def __str__(self):
    return self.usuario

class prenda(models.Model):
    marca   = models.ForeignKey(marca, on_delete= models.CASCADE, verbose_name= "nombre de la marca")
    talla = models.ForeignKey(talla,on_delete= models.CASCADE)  
    precio = models.FloatField(verbose_name="precio de la prenda")
    cantidad = models.IntegerField(verbose_name="cantidad a comprar")
    imagen = models.ImageField(verbose_name= "imagen", upload_to= "imgMujer")
    create = models.DateField(auto_now_add= True,verbose_name= "Fecha de creacion")
    update = models.DateField(auto_now= True,verbose_name= "Fecha edicion")
    class Meta:
        verbose_name = "prenda"
        verbose_name_plural = "prendas"
        ordering = ["-create"]   
    def __float__(self):
        return self.precio
    


class venta(models.Model):
    cliente = models.ForeignKey(cliente,on_delete= models.CASCADE)
    prenda = models.ForeignKey(prenda,on_delete= models.CASCADE)
    fecha = models.DateTimeField(verbose_name="fecha de la compra")
    create = models.DateField(auto_now_add= True,verbose_name= "Fecha de creacion")
    update = models.DateField(auto_now= True,verbose_name= "Fecha edicion")
class Meta:
    verbose_name = "venta"
    verbose_name_plural = "ventas"
    ordering = ["-create"]
def __str__(self):
    return self.venta