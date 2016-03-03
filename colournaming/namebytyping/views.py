from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Response, Time, User, Image, Patch
from django.template import Context
import random
import math
import time
from datetime import date

number_of_images = 40
total_time = 180

def index(request):
    request.session['already_seen'] = []
    request.session['count'] = 0
    request.session['survey_complete'] = "False"
    return render(request, 'namebytyping/index.html')

def survey(request):
    return render(request, 'namebytyping/survey.html')

def test_type(request):
    already_seen = request.session.get('already_seen')

    if request.session.get('in_progress') == "False":
        return HttpResponseRedirect(reverse('namebytyping:complete'))

    while True:
        image_number = random.choice(Patch.objects.values_list('id', flat=True))

        image_number = random.randint(1, number_of_images)

        if len(already_seen) == number_of_images:
            break;

        if image_number not in already_seen:
            patch = Patch.objects.get(id=image_number)
            image = patch.image
            already_seen.append(image_number)
            circlex = random.randint(patch.radius, image.width - patch.radius);
            circley = random.randint(patch.radius, image.height - patch.radius);

            request.session['already_seen'] = already_seen
            count = request.session.get('count')
            count += 1
            request.session['count'] = count
            return render(request, 'namebytyping/test_type.html', {'image_number' : image_number,
                                                                   'circlex' : circlex,
                                                                   'circley' : circley,
                                                                   'count' : count })

    request.session['already_seen'] = []
    request.session['end_time'] = time.time()
    return HttpResponseRedirect(reverse('namebytyping:complete'))

def test_speak(request):
    already_seen = request.session.get('already_seen')

    if request.session.get('in_progress') == "False":
        return HttpResponseRedirect(reverse('namebytyping:complete'))

    while True:
        image_number = random.choice(Patch.objects.values_list('id', flat=True))

        image_number = random.randint(1, number_of_images)

        if len(already_seen) == number_of_images:
            break;

        if image_number not in already_seen:
            patch = Patch.objects.get(id=image_number)
            image = patch.image
            already_seen.append(image_number)
            circlex = random.randint(patch.radius, image.width - patch.radius);
            circley = random.randint(patch.radius, image.height - patch.radius);

            request.session['already_seen'] = already_seen
            count = request.session.get('count')
            count += 1
            request.session['count'] = count
            return render(request, 'namebytyping/test_speak.html', {'image_number' : image_number,
                                                              'circlex' : circlex,
                                                              'circley' : circley,
                                                              'count' : count })

    request.session['already_seen'] = []
    request.session['end_time'] = time.time()
    return HttpResponseRedirect(reverse('namebytyping:complete'))

def test_speak_type(request):
    already_seen = request.session.get('already_seen')

    if request.session.get('in_progress') == "False":
        return HttpResponseRedirect(reverse('namebytyping:complete'))

    while True:
        image_number = random.choice(Patch.objects.values_list('id', flat=True))

        image_number = random.randint(1, number_of_images)

        if len(already_seen) == number_of_images:
            break;

        if image_number not in already_seen:
            patch = Patch.objects.get(id=image_number)
            image = patch.image
            already_seen.append(image_number)
            circlex = random.randint(patch.radius, image.width - patch.radius);
            circley = random.randint(patch.radius, image.height - patch.radius);

            request.session['already_seen'] = already_seen
            count = request.session.get('count')
            count += 1
            request.session['count'] = count
            return render(request, 'namebytyping/test_speak_type.html', {'image_number' : image_number,
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

def submit_type(request):
    colourname = request.POST['colourname']
    imagenumber = request.POST['imagenumber']
    user = User.objects.get(id=request.session.get('user'))
    data_to_save = Response(user=user, colour_name = colourname, image_number = imagenumber)
    data_to_save.save()
    return HttpResponseRedirect(reverse('namebytyping:test_type'))

def submit_speak(request):
    colourname = request.POST['colourname']
    imagenumber = request.POST['imagenumber']

    if colourname == "SPEECH-BROKEN":
        user = User.objects.get(id=request.session.get('user'))
        user.test_type = "type"
        user.save()
        request.session['already_seen'] = []
        request.session['start_time'] = time.time()
        return HttpResponseRedirect(reverse('namebytyping:test_type'))

    user = User.objects.get(id=request.session.get('user'))
    data_to_save = Response(user=user, colour_name = colourname, image_number = imagenumber)
    data_to_save.save()
    return HttpResponseRedirect(reverse('namebytyping:test_speak'))

def submit_speak_type(request):
    colourname = request.POST['colourname']
    imagenumber = request.POST['imagenumber']
    user = User.objects.get(id=request.session.get('user'))
    data_to_save = Response(user=user, colour_name = colourname, image_number = imagenumber)
    data_to_save.save()
    return HttpResponseRedirect(reverse('namebytyping:test_speak_type'))

def begin(request):

    gender = request.POST['gender']
    birth_year = request.POST['age']
    nationality = request.POST['nationality']

    if request.session.get('survey_complete') == "True":
        request.session['already_seen'] = []
        request.session['start_time'] = time.time()
        user = User.objects.get(id=request.session.get('user'))
        t_type = user.test_type
        if t_type == "type":
            return HttpResponseRedirect(reverse('namebytyping:test_type'))
        elif t_type == "speak":
            return HttpResponseRedirect(reverse('namebytyping:test_speak'))
        elif t_type == "speak_type":
            return HttpResponseRedirect(reverse('namebytyping:test_speak_type'))

    try:
        birth_year_int = int(birth_year)
        age = date.today().year - birth_year_int
    except ValueError:
        age = -1;

    has_speech_recog = request.POST['has-webkit']
    speech_consent = request.POST['speech-consent']
    test_type = "type"

    if has_speech_recog == "True" and speech_consent == "Yes":
        lottery = ["speak_type",
                   "speak_type",
                   "speak",
                   "speak",
                   "type"]
        test_type = lottery[random.randint(0, 4)]

    if gender == "Male" and speech_consent == "Yes":
        new_user = User(age=age, gender=User.MALE, nationality=nationality, willing_to_speak=User.WILLING_TO_SPEAK, test_type=test_type)
        new_user.save()
    elif gender == "Male" and speech_consent == "No":
        new_user = User(age=age, gender=User.MALE, nationality=nationality, willing_to_speak=User.UNWILLING_TO_SPEAK, test_type=test_type)
        new_user.save()
    elif gender == "Female" and speech_consent == "Yes":
        new_user = User(age=age, gender=User.FEMALE, nationality=nationality, willing_to_speak=User.WILLING_TO_SPEAK, test_type=test_type)
        new_user.save()
    elif gender == "Female" and speech_consent == "No":
        new_user = User(age=age, gender=User.FEMALE, nationality=nationality, willing_to_speak=User.UNWILLING_TO_SPEAK, test_type=test_type)
        new_user.save()
    elif gender == "no-say" and speech_consent == "Yes":
        new_user = User(age=age, gender=User.NO_SAY, nationality=nationality, willing_to_speak=User.WILLING_TO_SPEAK, test_type=test_type)
        new_user.save()
    elif gender == "no-say" and speech_consent == "No":
        new_user = User(age=age, gender=User.NO_SAY, nationality=nationality, willing_to_speak=User.UNWILLING_TO_SPEAK, test_type=test_type)
        new_user.save()

    request.session['user'] = new_user.id
    request.session['start_time'] = time.time()
    request.session['in_progress'] = "True"
    request.session['survey_complete'] = "True"

    if test_type == "type":
        return HttpResponseRedirect(reverse('namebytyping:test_type'))
    elif test_type == "speak":
        return HttpResponseRedirect(reverse('namebytyping:test_speak'))
    elif test_type == "speak_type":
        return HttpResponseRedirect(reverse('namebytyping:test_speak_type'))

def next(request):
    return HttpResponseRedirect(reverse('namebytyping:survey'))

def complete(request):
    time = request.session.get('end_time') - request.session.get('start_time')
    user = User.objects.get(id=request.session.get('user'))
    time_to_save = Time(user = user, time_elapsed = time)
    time_to_save.save()
    request.session['in_progress'] = "False"
    return render(request, 'namebytyping/complete.html')

def rerun(request):
    return HttpResponseRedirect(reverse('namebytyping:index'))
