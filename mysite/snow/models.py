# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Snow(models.Model):
    title = models.CharField(max_length=255,default='',blank=True)
    #description =  models.TextField(default='',blank=True)

    def __str__(self):
        return '%s ' % self.title



class Snowcar(models.Model):
    carnum = models.CharField(max_length=255,default='',blank=True)
    #description =  models.TextField(default='',blank=True)

    def __str__(self):
        return '%s ' % self.carnum

class userinput(models.Model):
    loc = models.CharField(default= '',max_length=20)
    num = models.CharField(default= '',max_length=20)

