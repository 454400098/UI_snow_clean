# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import SnowForm,Snowcarform, Snowdata
from .models import Snow
# Create your views here.



#def add_snow(request):
#    if request.method == "POST":
#        form1 = SnowForm(request.POST)
 #       if form1.is_valid():
#            snow_item=form1.save(commit=False)
#            snow_item.save()


#    else:
#        form1 = SnowForm()
 #   return render(request,'snow/snow_form.html', {'form':form1})


def add_snow(request):
    if request.method == "POST":
        form = Snowdata(request.POST)
        if form.is_valid():
            pass
    else:
        form=Snowdata()
    return render(request,'snow/snow_form.html', {'form':form})

def edit_snow(request,id=None):
    item = get_object_or_404(Snow,id=id) #return object with id or raist 404 error
    form = SnowForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()

    return render(request,'snow/snow_form.html',{'form':form})

