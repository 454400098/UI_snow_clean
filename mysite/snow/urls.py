from django.conf.urls import url
from django.contrib import admin
from . import views
admin.autodiscover()
from django.contrib.auth.views import login
urlpatterns = [
    #url(r'^$', views.index, name='index'),

    url(r'^login/$',login,{'template_name': 'snow/login.html'}),
    url(r'^add/snow/$',views.add_snow, name='add_snow'),
    url(r'^result/$', views.result, name='result'),
    url(r'^result2/$', views.result2, name='result2'),
    url(r'^edit/snow/(?P<id>\d+)/$', views.edit_snow, name='edit_snow'), #we're sending variable
 #   url(r'^snow/(?P<id>\d+)/$', views.snow, name='snow'),

]