from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Response
from django.template import Context

def index(request):
    image_number = 1
    return render(request, 'namebytyping/index.html', {'image_number' : image_number})

def results(request):
    responses = Response.objects.all()
    return render(request, 'namebytyping/results.html', {'responses': responses})

def submit(request):
    colourname = request.POST['colourname']
    imagenumber = request.POST['imagenumber']
    data_to_save = Response(colour_name = colourname, image_number = imagenumber)
    data_to_save.save()
    return HttpResponseRedirect(reverse('namebytyping:results'))
