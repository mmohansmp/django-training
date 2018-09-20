# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Request(models.Model):
    created_at = models.DateTimeField(default=timezone.now) 
    updated_at = models.DateTimeField(default=timezone.now)
    command    = models.CharField(max_length = 50, default='')
    user       = models.CharField(max_length = 50, default='')
    password   = models.CharField(max_length = 50, default='')
