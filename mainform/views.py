from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
@login_required
def mainform(request):
    return HttpResponse("123")
