from django.forms import ModelForm
from .models import Snow, Snowcar,userinput
from django import forms

class SnowForm(ModelForm):
    class Meta:
        model = Snow
        fields = ['title']

class Snowcarform(ModelForm):
    class Meta:
        model = Snowcar
        fields = ['carnum']

class Snowdata(forms.ModelForm):
  # address = forms.CharField(max_length=30)
  #  numcar = forms.CharField(max_length=10)
      class Meta:
        model=userinput
        fields = ['loc','num']