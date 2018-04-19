from django.forms import ModelForm
from .models import Snow

class SnowForm(ModelForm):
    class Meta:
        model = Snow
        fields = ['title']

