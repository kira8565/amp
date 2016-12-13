from django.conf.urls import url
from django.contrib import admin

from account import views
from account.views import login

urlpatterns = [
    url(r'^checkLogin$', views.checkLogin, name='checkLogin'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^', views.login, name='account'),
]
