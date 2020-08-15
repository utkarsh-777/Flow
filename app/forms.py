from .models import PostModel
from django.forms import ModelForm

class Postform(ModelForm):
    class Meta:
        model = PostModel
        fields = ['PostTitle','PostDescription','PostImage']