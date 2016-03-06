from django.conf.urls import url

from . import views

app_name = 'namebytyping'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^results/$', views.results, name='results'),
    url(r'^submit_speak/$', views.submit_speak, name='submit_speak'),
    url(r'^submit_type/$', views.submit_type, name='submit_type'),
    url(r'^submit_speak_type/$', views.submit_speak_type, name='submit_speak_type'),
    url(r'^test_speak_type/$', views.test_speak_type, name='test_speak_type'),
    url(r'^test_speak/$', views.test_speak, name='test_speak'),
    url(r'^test_type/$', views.test_type, name='test_type'),
    url(r'^begin/$', views.begin, name='begin'),
    url(r'^complete/$', views.complete, name='complete'),
    url(r'^rerun/$', views.rerun, name='rerun'),
    url(r'^survey/$', views.survey, name='survey'),
    url(r'^next/$', views.next, name='next'),
    url(r'^test_speak_info/$', views.test_speak_info, name='test_speak_info'),
    url(r'^test_type_info/$', views.test_type_info, name='test_type_info'),
    url(r'^test_speak_type_info/$', views.test_speak_type_info, name='test_speak_type_info'),
    url(r'^start_speak/$', views.start_speak, name='start_speak'),
    url(r'^start_type/$', views.start_type, name='start_type'),
    url(r'^start_speak_type/$', views.start_speak_type, name='start_speak_type'),
]
