from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Response, Time, User, Image, Patch
from django.template import Context
import random
import math
import time

number_of_images = 40
total_time = 180

def index(request):
    request.session['already_seen'] = []
    request.session['count'] = 0
    new_user = User(age=0, gender=User.FEMALE, nationality='British')
    new_user.save()
    request.session['user'] = new_user.id
    return render(request, 'namebytyping/index.html')

def test(request):
    already_seen = request.session.get('already_seen')

    while True:
        image_number = random.choice(Patch.objects.values_list('id', flat=True))

        if len(already_seen) == number_of_images:
            break;

        if image_number not in already_seen:
            patch = Patch.objects.get(id=image_number)
            image = patch.image
            already_seen.append(image_number)
            #next two lines is the code to determing the centre of the circle drawn on the image
            circlex = random.randint(patch.radius, image.width - patch.radius); #circle cannot leave image, so centre must be at least 20 from edge
            circley = random.randint(patch.radius, image.height - patch.radius);

            request.session['already_seen'] = already_seen
            count = request.session.get('count')
            count += 1
            request.session['count'] = count
            return render(request, 'namebytyping/test.html', {'image_number' : image_number,
                                                              'circlex' : circlex,
                                                              'circley' : circley,
                                                              'count' : count })

    request.session['already_seen'] = []
    request.session['end_time'] = time.time()
    return HttpResponseRedirect(reverse('namebytyping:complete'))

def results(request):
    for user in User.objects.all():
        if len(Response.objects.filter(user=user)) == 0:
            user.delete()
    responses = Response.objects.all()
    times = Time.objects.all()
    images_count = []
    for i in range(1, number_of_images + 1):
        images_count.append(i)
    return render(request, 'namebytyping/results.html', {'responses': responses,
                                                         'images_count' : images_count,
                                                         'times' : times})

def submit(request):
    colourname = request.POST['colourname']
    imagenumber = request.POST['imagenumber']
    user = User.objects.get(id=request.session.get('user'))
    data_to_save = Response(user=user, colour_name = colourname, image_number = imagenumber)
    data_to_save.save()
    return HttpResponseRedirect(reverse('namebytyping:test'))

def begin(request):
    request.session['start_time'] = time.time()
    return HttpResponseRedirect(reverse('namebytyping:test'))

def complete(request):
    time = request.session.get('end_time') - request.session.get('start_time')
    time_to_save = Time(time_elapsed = time)
    time_to_save.save()
    return render(request, 'namebytyping/complete.html')

def rerun(request):
    return HttpResponseRedirect(reverse('namebytyping:index'))
