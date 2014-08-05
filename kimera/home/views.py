from django.shortcuts import render, render_to_response
from django.template import RequestContext
from .models import SlideHome

def Home(request):
	slides = SlideHome.objects.filter(activo=True).order_by('orden')
	return render_to_response('home.html',locals(),context_instance=RequestContext(request))