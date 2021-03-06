# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login
from models import Request



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
    context = {
                 'req': req
              }
    return HttpResponse(template.render(context, req))

def process(req):
    if req.GET['name'] == 'adcmd':
        template = loader.get_template('ad-hoc.html')
    elif req.GET['name'] == 'another'  :
        template = loader.get_template('another.html')
    else:
        template = loader.get_template('nproc.html')
    context = {
                 'req': req
              }
    return HttpResponse(template.render(context, req))
def main_block(req):
    template = loader.get_template('main.html')
    context = {
                 'req': req
              }
    return HttpResponse(template.render(context, req))

def request(req):
    if req.method == 'POST':
        ureq = Request(user=req.POST['username'],
                      password=req.POST['password'],
                      command=req.POST['command'] )
        ureq.save()
        template = loader.get_template('request.html')
        context = {
                 'req': req,
                 'ureq': ureq
              }
        return HttpResponse(template.render(context, req))
