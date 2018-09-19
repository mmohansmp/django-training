# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse



# Create your views here.

def index(req):
    return HttpResponse('<h1>Hello World from (String)</h1>')

def index_html(req):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({ 'name':'Mohan', 'req':  req}, req))
