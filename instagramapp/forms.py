from django import forms
from .models import Image,Profile,Comment


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes','image_comment','profile','user', 'created_date']
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=['user','image']