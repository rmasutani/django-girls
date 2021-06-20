from django import forms
from django.forms import fields
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        """
        DjangoにどのModelを使うべきか伝える(model=Post)クラス
        """
        model = Post
        fields = ('title', 'text')
