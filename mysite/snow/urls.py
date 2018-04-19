from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^add/snow/$',views.add_snow, name='add_snow'),
    url(r'^edit/snow/(?P<id>\d+)/$', views.edit_snow, name='edit_snow'), #we're sending variable


]