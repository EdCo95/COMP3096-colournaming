from django.conf.urls import url

from . import views

app_name = 'namebytyping'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^results/$', views.results, name='results'),
    url(r'^submit/$', views.submit, name='submit'),
    url(r'^test/$', views.test, name='test'),
    url(r'^begin/$', views.begin, name='begin'),
    url(r'^complete/$', views.complete, name='complete'),
    url(r'^rerun/$', views.rerun, name='rerun'),
]
