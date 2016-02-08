from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Response
from django.template import Context
import random
import math

already_seen = []
number_of_images = 11
time_elapsed = 0
total_time = 180

def index(request):
    return render(request, 'namebytyping/index.html')

def test(request):

    while True:
        image_number = random.randint(1, number_of_images)
        if len(already_seen) == number_of_images:
            break;
        elif time_elapsed == "-1":
            break;

        if image_number not in already_seen:
            already_seen.append(image_number)
            time_remaining = total_time - int(time_elapsed)
            minutes = int(math.floor(time_remaining / 60))
            seconds = int(time_remaining - minutes * 60)
            #next two lines is the code to determing the centre of the circle drawn on the image
            circlex = random.randint(20,280); #circle cannot leave image, so centre must be at least 20 from edge
            circley = random.randint(20,380);

            if seconds == 0:
                time = "0" + str(minutes) + ":" + str(seconds) + "0"
            else:
                time = "0" + str(minutes) + ":" + str(seconds)

            return render(request, 'namebytyping/test.html', {'image_number' : image_number,
                                                              'time_elapsed' : time_elapsed,
                                                              'time' : time,
                                                              'circlex' : circlex,
                                                              'circley' : circley})

    global time_elapsed
    global already_seen
    del already_seen[:]
    time_elapsed = 0;
    return HttpResponseRedirect(reverse('namebytyping:complete'))

def results(request):
    responses = Response.objects.all()
    return render(request, 'namebytyping/results.html', {'responses': responses})

def submit(request):
    colourname = request.POST['colourname']
    imagenumber = request.POST['imagenumber']
    time = request.POST['timer']
    global time_elapsed
    time_elapsed = time
    data_to_save = Response(colour_name = colourname, image_number = imagenumber)
    data_to_save.save()
    return HttpResponseRedirect(reverse('namebytyping:test'))

def begin(request):
    return HttpResponseRedirect(reverse('namebytyping:test'))

def complete(request):
    return render(request, 'namebytyping/complete.html')

def rerun(request):
    return HttpResponseRedirect(reverse('namebytyping:index'))
