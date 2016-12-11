from django.conf.urls import url
from django.contrib import admin

from mainform import views

urlpatterns = [
    url(r'^', views.mainform, name='mainform'),
]
