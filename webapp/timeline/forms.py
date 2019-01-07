from django import forms
from django.core.exceptions import ValidationError
from timeline.models import posts,Document,User,Like

class loginForm(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(max_length=50,widget=forms.PasswordInput)


class addPost(forms.ModelForm):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=50)
    image_url = forms.CharField(max_length=50)
    class Meta:
        model= posts
        fields=('title','description','image_url')

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title','description', 'document', )


# class LikeForm(forms.ModelForm):
#     class Meta:
#         model = Like




