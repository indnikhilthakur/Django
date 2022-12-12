from django import forms
from .models import *

class ImageForm(forms.ModelForm):
    class Meta:
        model=model_practice4
        fields=("name_char_field3","image_field")