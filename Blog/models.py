from django.db import models

from django.utils import timezone 

"""@reciver(post_delete,sender=Post)
def Post_delete(sender, instance, **kwargs):
	instance.Post.delete(False)

class Categoria_Post(models.Model):
	nombre = models.CharField(max_length=40)
	def __unicode__(self):
		return self.nombre"""

class Post(models.Model):
	autor = models.ForeignKey('auth.User')
	titulo_post = models.CharField(max_length=140, blank=True, null=True)
	articulo = models.TextField(blank=True,null=True)
	fecha_creacion = models.DateTimeField(default=timezone.now)
	fecha_publicacion = models.DateTimeField(blank=True, null=True)
	def publish(self):
		self.fecha_publicacion = timezone.now()
		self.save()
	def __str__(self):
		return self.titulo_post
		

