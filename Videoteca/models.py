from django.db import models
from django.dispatch import receiver

"""@reciver(post_delete,sender=otografia)
def Foto_delete(sender, instance, **kwargs):
	instance.Foto.delete(False)"""

class Categoria_Video(models.Model):
	nombre = models.CharField(max_length=40)
	def __unicode__(self):
		return self.nombre

class Video(models.Model):
	categoria_video = models.ForeignKey(Categoria_Video, null=True, blank=True)
	titulo_video = models.CharField(max_length=40, default='Sin título', null=True, blank=True)
	video = models.FileField(upload_to='videos/', null=True, blank=True)
	url_video = models.URLField(null=True, blank=True)
	fecha_pub_video = models.DateField(auto_now_add=True)
	descripcion = models.CharField(max_length=140, null=True, blank=True)
	def publish(self):
		self.fecha_pub_video = timezone.now()
		self.save()
	def __unicod__(self):
		self.save()
		return self.titulo_video
