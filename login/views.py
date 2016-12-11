from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def login(request):
    return render(request, 'login/login.html')


def checkLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect("/mainform")
    elif user and user.is_active == False:
        return render(request, 'login/login.html', context={
            'msg': "该用户已被禁用"
        })
    else:
        return render(request, 'login/login.html', context={
            'msg': "用户名密码有误"
        })
