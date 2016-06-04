from django.shortcuts import render
from django.utils import timezone 
from .models import Fotografia

def fotos_list(request):
	fotos = Fotografia.objects.filter(published_date_lte=timezone.now()).order_by('fecha_bub')
	return render (request, 'fotos/fotos_list.html',{'fotos':fotos})