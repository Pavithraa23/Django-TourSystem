from django import forms
from .models import Tour
from django.contrib.auth.models import User
from .models import UserProfile, Comment

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class ProfileForm(forms.ModelForm):
    avatar = forms.ImageField(required=False)  # Include the avatar field

    class Meta:
        model = User
        fields = ['username', 'email', 'avatar']


class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ['title', 'duration', 'price', 'description','image','latitude', 'longitude'] 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'rating'] 