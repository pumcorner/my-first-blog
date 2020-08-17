from django import forms
from .models import Post
from .models import Personal_info

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','text',)

class InfoForm(forms.ModelForm):

    class Meta:
        model = Personal_info
        fields = ('title','pic','mobile','email','my_words')
