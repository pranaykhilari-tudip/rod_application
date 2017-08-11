# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from allauth.account.views import SignupView, LoginView, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render

from rodapp.forms import *

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')

class UserSignup(SignupView):
    template_name = 'signup.html'
    form_class = UserSignupForm

class UserLogin(LoginView):
    template_name = 'login.html'
    form_class = UserLoginForm

def is_user_authenticated(request):
    if request.user.is_anonymous():
        return HttpResponseRedirect('/accounts/login/')
    else:
       return render(request, 'dashboard.html')

