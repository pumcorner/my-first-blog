from django import forms
from .models import Post
from .models import Personal_info
from .models import Work_detail, Guest_post
from .models import Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','author','text',)

class InfoForm(forms.ModelForm):

    class Meta:
        model = Personal_info
        fields = ('title','pic','mobile','email','my_words',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author','text',)

class RecordForm(forms.ModelForm):

    class Meta:
        model = Work_detail
        fields = ('title','duration','details',)

class GuestForm(forms.ModelForm):

    class Meta:
        model = Guest_post
        fields = ('title','author','text',)
