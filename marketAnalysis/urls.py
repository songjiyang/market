from django.conf.urls import url
# -*- coding: utf-8 -*-
from . import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
]