from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

@reciver(post_delete,sender=Fotografia)
def Foto_delete(sender, instance, **kwargs):
	instance.Foto.delete(False)

class Categoria(models.Model):
	nombre = models.CharField(max_length=40)
	def __unicode__(self):
		return self.nombre

class Fotografia(models.Model):
	categoria = models.ForeignKey(Categoria, null=True, blank=True)
	titulo_foto = models.CharField(max_length=40, default='Sin título', null=True, blank=True)
	foto = models.ImageField(upload_to='Fotos/')
	fecha_pub = models.DateField(auto_now_add=True)
	comentario = models.CharField(max_length=140, null=True, blank=True)
	def publish(self):
		self.fecha_pub = timezone.now()
		self.save()
	def __unicod__(self):
		return self.titulo_foto