from django.forms import forms,ModelForm
from Base.models import *

class PostCreateFrom(ModelForm):
    class Meta:
        model=Post
        fields='__all__'


