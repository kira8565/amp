from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

# 登录页面
from login.forms import loginForm


def login(request):
    return render(request, 'login/login.html', {
        'form': loginForm()
    })


# 登录检查
def checkLogin(request):
    form = loginForm(request)
    if form.is_valid():
        form = loginForm()
        return render(request, 'login/login.html', context={
            'msg': "用户名密码有误",
            'form': form
        })

    else:
        user = auth.authenticate(username=form.username, password=form.password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect("/mainform")

        elif user and user.is_active == False:
            return render(request, 'login/login.html', context={
                'msg': "该用户已被禁用",
                'form': form
            })
        else:
            return render(request, 'login/login.html', context={
                'msg': "用户名密码有误",
                'form': form
            })


# 用户登出
def logout(request):
    auth.logout(request)
    return render(request, 'login/login.html', context={
        'info': "登出成功"
    })
