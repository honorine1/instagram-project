from django import forms
from .models import Image,Profile


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes','image_comment','profile','user', 'created_date']
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']