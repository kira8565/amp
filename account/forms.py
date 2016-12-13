# -*- coding: utf-8 -*-
from django import forms
from hpwidget import widgets


class loginForm(forms.Form):
    username = forms.CharField(widget=widgets.HpInputWidget(
        attrs={
            'placeholder': '用户名'
        }),
        label='')
    password = forms.CharField(widget=widgets.HpInputWidget(
        attrs={'placeholder': '密码', 'type': 'password'}),
        label='')
