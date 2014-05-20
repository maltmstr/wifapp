from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views import generic

def index(request):
	template = loader.get_template('index.html')
	context = RequestContext(request, {
		#'latest_poll_list': latest_poll_list,
	})
	return HttpResponse(template.render(context))

#class IndexView(generic.ListView):
#	template_name = 'wifapp/index.html'


