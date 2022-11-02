from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    #Carrera = models.TextField()
    #Año = models.TextField()
    #Correlativo = models.TextField()
    #Contraseña = models.TextField()

