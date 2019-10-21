# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .forms import ImageForm, ProfileForm
import datetime as dt
from .models import User,Image,Profile,Follower
from django.contrib.auth.decorators import login_required
from django.http  import HttpResponse,HttpResponseRedirect



# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    
    return render(request,'my-instagram/index.html')

@login_required(login_url='/accounts/login/')
def posts(request, post_id):
    try:
        # posts = Image.objects.all().order_by('created_date')
        posts = Image.objects.get(id = post_id)
        # return redirect('index.html')
    except DoesNotExist:
        raise Http404()
    return render(request,"my-instagram/post.html", {"posts":posts})


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    # profile = Profile
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
            return redirect('postsToday/')

    else:
        form = ImageForm()
    return render(request, 'my-instagram/new_post.html', {"form": form})






def posts_today(request):
    date = dt.date.today()
    posts = Image.todays_posts()
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            image = form.cleaned_data['your_image']
            image_description = form.cleaned_data['image_description']
            # recipient = NewsLetterRecipients(name = name,email =email)
            # recipient.save()
            # send_welcome_email(name,email)
            return redirect('new/post/postToday/')
    else:
        form = ImageForm()
    return render(request, 'my-instagram/today-post.html', {"date": date,"posts":posts,"letterForm":form})

@login_required(login_url='/accounts/login/')
def profile(request,profile_id):

    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect('index')

    else:
        form = ProfileForm()

    user=User.objects.all()

    images = Image.objects.filter(profile = profile_id)
    # title = User.objects.get(user = current_user).username
    profile = Profile.objects.filter(user = profile_id)

    # if Follower.objects.filter(followings=request.user,followers=user).exists():
    #     is_follow=True
    # else:
    #     is_follow=False

    # followerss=Follower.objects.filter(followers = user).count()
    # followingss=Follower.objects.filter(followings=user).count()


    # return render(request,"my-instagram/profile.html",{"user":user})
    return render(request,"my-instagram/profile.html",{"user":user,"images":images,"profile":profile})


# @login_required(login_url='/accounts/login/')
# def updateProfile(request):

#     current_user=request.user
#     if request.method =='POST':
#         if Profile.objects.filter(user_id=current_user).exists():
#             form = UpdateProfile(request.POST,request.FILES,instance=Profile.objects.get(user_id = current_user))
#         else:
#             form=UpdateProfile(request.POST,request.FILES)
#         if form.is_valid():
#           profile=form.save(commit=False)
#           profile.user=current_user
#           profile.save()
#           return redirect('profile',current_user.id)
#     else:

#         if Profile.objects.filter(user_id = current_user).exists():
#            form=UpdateProfile(instance =Profile.objects.get(user_id=current_user))
#         else:
#             form=UpdateProfile()

#     return render(request,'all-views/update.html',{"form":form})        
