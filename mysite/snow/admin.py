# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Snow, Snowcar,userinput
# Register your models here.

admin.site.register(Snow)
admin.site.register(Snowcar)
admin.site.register(userinput)