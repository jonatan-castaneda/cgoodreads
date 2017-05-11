from django.db import models
from modules.authors.models import Author
from django.conf import settings

# Create your models here.
class Book(models.Model):
    GENEROS = (
        ("CM", "Comedia"),
        ("TR", "Terror"),
        ("DR", "Drama")
    )
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 150)
    autor = models.ForeignKey(Author,
        on_delete = models.CASCADE)
    isbn = models.CharField(max_length = 150, unique=True)
    fecha_pub = models.DateField()
    foto = models.URLField(max_length = 250)
    descripcion = models.TextField()
    rating = models.FloatField(null=True, blank=True)
    #rating = models.DecimalField(max_digits = 3, decimal_places=2, default=0.00)

    genero = models.CharField(choices = GENEROS, max_length = 20)

    def __str__(self):
        return "Libro: %s" % (self.nombre)

class Comments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE, related_name = "comentarios")
    comentario = models.TextField()