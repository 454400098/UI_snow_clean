from django.forms import ModelForm
from .models import Snow, Snowcar,userinput
from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class SnowForm(ModelForm):
    class Meta:
        model = Snow
        fields = ['title']

class Snowcarform(ModelForm):
    class Meta:
        model = Snowcar
        fields = ['carnum']

#class Snowdata(forms.ModelForm):
  # address = forms.CharField(max_length=30)
  #  numcar = forms.CharField(max_length=10)
     # class Meta:
     #   model=userinput
     #   fields = ['loc','num']


def validate_positive(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s is not a positive number'),
            params={'value': value},
        )


def validate_string(value):
    if isinstance(value,str)== 0:
        raise ValidationError(
            _('%(value)s is not a valid address, please try again'),
            params={'value': value},
        )

class Snowdata(forms.Form):
    loc = forms.CharField(label='Working address',max_length=20)
    num = forms.IntegerField(label='Number of cars',validators=[validate_positive])
    #st = forms.CharField(label='Start',max_length=10)
    #en = forms.CharField(label='End',max_length=10)

