from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Response
from django.template import Context
import random
import math

number_of_images = 11
total_time = 180

def index(request):
    request.session['already_seen'] = []
    request.session['time_elapsed'] = 0
    request.session['count'] = 0
    return render(request, 'namebytyping/index.html')

def test(request):
    already_seen = request.session.get('already_seen')
    time_elapsed = request.session.get('time_elapsed')
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

            if seconds == 0:
                time = "0" + str(minutes) + ":" + str(seconds) + "0"
            else:
                time = "0" + str(minutes) + ":" + str(seconds)

            request.session['already_seen'] = already_seen
            count = request.session.get('count')
            count += 1
            request.session['count'] = count
            return render(request, 'namebytyping/test.html', {'image_number' : image_number,
                                                              'time_elapsed' : time_elapsed,
                                                              'time' : time,
                                                              'count' : count })

    request.session['already_seen'] = []
    request.session['time_elapsed'] = 0;
    return HttpResponseRedirect(reverse('namebytyping:complete'))

def results(request):
    responses = Response.objects.all()
    images_count = []
    for i in range(1, number_of_images + 1):
        images_count.append(i)
    return render(request, 'namebytyping/results.html', {'responses': responses,
                                                         'images_count' : images_count})

def submit(request):
    colourname = request.POST['colourname']
    imagenumber = request.POST['imagenumber']
    time = request.POST['timer']
    request.session['time_elapsed'] = time
    data_to_save = Response(colour_name = colourname, image_number = imagenumber)
    data_to_save.save()
    return HttpResponseRedirect(reverse('namebytyping:test'))

def begin(request):
    return HttpResponseRedirect(reverse('namebytyping:test'))

def complete(request):
    return render(request, 'namebytyping/complete.html')

def rerun(request):
    return HttpResponseRedirect(reverse('namebytyping:index'))
