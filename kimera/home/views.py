from django.shortcuts import render, render_to_response
from django.template import RequestContext
from .models import SlideHome

from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
	template_name = "home.html"

	def get_context_data(self,**kwargs):
		context = super(HomePageView, self).get_context_data(**kwargs)
		context['slides'] = SlideHome.objects.filter(activo=True).order_by('orden')
		return context

