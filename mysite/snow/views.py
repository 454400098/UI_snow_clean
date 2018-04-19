# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import SnowForm,Snowcarform, Snowdata
from .models import Snow
from .models import userinput
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
    if request.method == "GET":
        form = Snowdata(request.GET)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/result')
    else:
        form=Snowdata()
    return render(request,'snow/snow_form.html', {'form':form})

def result(request):
    re=userinput.objects.all
    return render(request,'snow/result.html', {'result':re})

def edit_snow(request,id=None):
    item = get_object_or_404(Snow,id=id) #return object with id or raist 404 error
    form = SnowForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()

    return render(request,'snow/snow_form.html',{'form':form})

