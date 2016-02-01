from django.shortcuts import render
from django.http import HttpResponse
from .models import Response

def index(request):
    return render(request, 'namebytyping/index.html')

def results(request):
    responses = Response.objects.all()
    return render(request, 'namebytyping/results.html', {'responses': responses})
