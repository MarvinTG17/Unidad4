from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

class Proyecto (models.Model):
    titulo          = CharField(max_length=100)
    descripcion     = CharField(max_length=250)
    imagen          = ImageField(upload_to="proyectos/imagenes/",null=True)
    url             = URLField(blank=True)
    tipo_proyecto   = CharField(max_length=50,default="")




