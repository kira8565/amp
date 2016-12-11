from django import forms


class loginForm(forms.Form):
    username = forms.CharField(error_messages={'required': '请填写用户名'})
    password = forms.CharField(error_messages={'required': '请填写密码'})
