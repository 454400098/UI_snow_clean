# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import SnowForm,Snowcarform, Snowdata
from .models import Snow
from .models import userinput
import osmnx as ox
from PIL import Image

##################
import os
##########################


from snow_main.snow_clearance import snow_clearance

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
    #if os.path.exists('snow/static/snow/images/temp1.png'):
               # os.remove('snow/static/snow/images/temp1.png')
    if request.method == "GET":
        form = Snowdata(request.GET)

        if form.is_valid():
            place = form.cleaned_data['loc']
            k = int(form.cleaned_data['num'])
            #plot1(place, k)
            pp_1= int(form.cleaned_data['st'])
            pp_2 = int(form.cleaned_data['en'])
            #pp_1=1
            #pp_2=98
            snow_clearance(k,place,pp_1,pp_2)
            #form.save()
            return HttpResponseRedirect('/result',{'form':form})
    else:
        form=Snowdata()
    return render(request,'snow/snow_form.html', {'form':form})

def result(request):
    re=Snowdata(request.GET)


   #plot(add_snow.location, add_snow.number)
    return render(request,'snow/result.html', {'result':re})

def result2(request):
    re=Snowdata(request.GET)


   #plot(add_snow.location, add_snow.number)
    return render(request,'snow/result2.html', {'result':re})

def edit_snow(request,id=None):
    item = get_object_or_404(Snow,id=id) #return object with id or raist 404 error
    form = SnowForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()

    return render(request,'snow/snow_form.html',{'form':form})


#snow_clearance("Rutgers University",3,1,98)


def plot1(location,number):
    place = location
    k = number
    G = ox.graph_from_address(place, network_type='drive')
    ox.plot_graph(G, save=True, file_format='png', filename='temp2', show=False)
    im = Image.open('images/temp2.png')
    im.save('snow/static/snow/images/temp1.png','png')

#####################################################################
