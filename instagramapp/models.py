# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime as dt
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    profile_pic = models.ImageField(default='default.jpg',upload_to = 'profile_pics/', blank=True)
    profile_bio = models.CharField(max_length =100,null=True)
    # user = models.ForeignKey(User,on_delete=models.CASCADE)

    
    def __str__(self):
        return self.user.username
    

    def save_profile(self):
        self.save()

    @classmethod
    def delete_profile(cls,profile):
        cls.objects.filter(profile=profile).delete()

    @classmethod
    def search_by_username(cls,search_term):
        user = cls.objects.filter(user__username__icontains=search_term)
        return user
    
class Image(models.Model):
    image = models.ImageField(upload_to='instagram_photos/', blank=True, null=True)
    image_name = models.CharField(max_length = 50)
    image_caption = HTMLField()
    # image_caption = models.CharField(max_length = 50)
    likes = models.IntegerField(default=None,null=True)
    image_comment = models.CharField(max_length = 1000)
    profile = models.ForeignKey(Profile,null=True) 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.image_name 
    def save_image(self):
        self.save()


  
   
    
    @classmethod
    def delete_image(cls,image):
        cls.objects.filter(image=image).delete()

    @classmethod
    def update_image(cls,id,image):
        images=cls.objects.filter(image_id=id).update(image_image = image)
        return images

    @classmethod
    def todays_posts(cls):
        today = dt.date.today()
        posts = cls.objects.filter(created_date__date = today)
        return posts

    @classmethod
    def days_posts(cls,date):
        posts = cls.objects.filter(created_date__date = date)
        return posts
    
   
 

class Follower(models.Model):
    followers = models.IntegerField(default=None)
    followings = models.IntegerField(default=None)
    profile = models.ForeignKey(Profile)

    def __str__(self):
        return self.followers

    def save_follower(self):
        self.save()
    
    @classmethod
    def delete_follower(cls,follower):
        cls.objects.filter(follower=follower).delete()

    
    def __str__(self):
        return self.followers 

