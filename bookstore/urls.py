from .views import *
from . import views
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^$', views.index, name='index')
]

urlpatterns = format_suffix_patterns(urlpatterns)