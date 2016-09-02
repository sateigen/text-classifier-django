from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^classifier/(?P<pk>[0-9]+)$', views.classifier, name='classifier'),
    url(r'^trainer/(?P<pk>[0-9]+)$', views.trainer, name='trainer'),
]
