# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login



# Create your views here.

def index(req):
    return HttpResponse('<h1>Hello World from (String)</h1>')

def index_html(req):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({ 'name':'Mohan', 'req':  req}, req))

def auth(req):
    if req.method == 'GET':
        template = loader.get_template('login.html')
        return HttpResponse(template.render({ 'name':'Mohan', 'req':  req}, req))
    if req.method == 'POST':
       username = req.POST['username']
       password = req.POST['password']
       user = authenticate(username=username, password=password)
       if user is not None:
           login(req, user)
           return HttpResponseRedirect('/appone/home/')
       else:
           return HttpResponseRedirect('/appone/authenticate/')

def home(req):
    template = loader.get_template('layout.html')
    return HttpResponse(template.render({ 'req':  req}, req))
