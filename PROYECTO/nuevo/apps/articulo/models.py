from datetime import timezone
from django.db import models

# Create your models here.

class Categoria(models.Model):
      nombre=models.CharField(max_length=30,null=False)


class articulo(models.Model):
    #self.id_usuario = usuario_actual[0]
    #self.nombre_usuario = usuario_actual[1]
    titulo = models.CharField(max_lenght=30, null=True)
    resumen = models.TextField(null=False)
    contenido = models.TextField(null=False)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(null=True,blank=True,upload_to='media/articulo',default='media/articulo/default_articulo.jpg')
    estado = models.BooleanField(default=True)
    categoria=models.ForeignKey(Categoria,on_delete=models.SET_NULL, null=True, default='Sin categoría')
    publicado=models.DateTimeField(default=timezone.now)

    class Meta:
        ordering=('-publicado',)
    def __str__(self):
        return self.titulo
    def delete(self,using=None,keep_parents=False):
        self.imagen.delete(self.imagen.name)
        super().delete()
        

    

    def publicar (self):
        self.articulo.append(self.id_articulo)
        self.articulo.append(self.id_usuario)
        self.articulo.append(self.titulo)
        self.articulo.append(self.resumen)
        self.articulo.append(self.contenido)
        self.articulo.append(self.fecha_publicacion)
        self.articulo.append(self.imagen)
        self.articulo.append(self.estado)
        self.articulo.append(self.nombre_usuario)
        self.articulos.append(self.articulo)
        


def menu_off():
    print("================================")
    print("1. Registrarse como Colaborador")
    print("2. Registrarse como Público")
    print("3. Iniciar sesión")
    print("4. Salir")
    print("================================")
    

def menu_on():
    print("================================")
    print("1.Publicar")
    print("2.Buscar Articulo")
    print('3.Cerrar Sesion')
    print("================================")
