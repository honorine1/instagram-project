# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .forms import ImageForm, ProfileForm,CommentForm
import datetime as dt
from .models import User,Image,Profile,Follower
from django.contrib.auth.decorators import login_required
from django.http  import HttpResponse,HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm,AuthenticationForm




# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    images= Image.objects.all().order_by("created_date")
    profile= Profile.objects.all()
    # comments=Comment.objects.all()
    

    # if request.method == 'POST':
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         post_id = int(request.POST.get("idpost"))
    #         post = Post.objects.get(id = post_id)
    #         comment = form.save(commit=False)
    #         comment.user = request.user
    #         comment.post = post
    #         comment.save()
    #         return redirect('index')

    #     else:
    #         form = CommentForm()




    
    return render(request,'my-instagram/index.html',{"images":images})

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
            return redirect('index')

    else:
        form = ImageForm()
    return render(request, 'my-instagram/new_post.html', {"form": form})






# def posts_today(request):
#     date = dt.date.today()
#     posts = Image.todays_posts()
#     if request.method == 'POST':
#         form = ImageForm(request.POST)
#         if form.is_valid():
#             image = form.cleaned_data['your_image']
#             image_description = form.cleaned_data['image_description']
#           ail)
#             return redirect('new/post/postToday/')
#     else:
#         form = ImageForm()
#     return render(request, 'my-instagram/today-post.html', {"date": date,"posts":posts,"letterForm":form})

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

    profile = Profile.objects.filter(user = profile_id)

    # if Follower.objects.filter(followings=request.user,followers=user).exists():
    #     is_follow=True
    # else:
    #     is_follow=False

    # followerss=Follower.objects.filter(followers = user).count()
    # followingss=Follower.objects.filter(followings=user).count()


    # return render(request,"my-instagram/profile.html",{"user":user})
    return render(request,"my-instagram/profile.html",{"user":user,"images":images,"profile":profile})


@login_required(login_url='/accounts/login/')
def updateProfile(request):

    current_user=request.user
    if request.method =='POST':
        if Profile.objects.filter(user_id=current_user).exists():
            form = ProfileForm(request.POST,request.FILES,instance=Profile.objects.get(user_id = current_user))
        else:
            form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
          profile=form.save(commit=False)
          profile.user=current_user
          profile.save()
          return redirect('profile',current_user.id)
    else:

        if Profile.objects.filter(user_id = current_user).exists():
           form=ProfileForm(instance =Profile.objects.get(user_id=current_user))
        else:
            form=ProfileForm()

    return render(request,'my-instagram/update_profile.html',{"form":form}) 

@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        searched_user = Profile.search_by_username(search_term)
        message = f"{search_term}"

        return render(request, 'my-instagram/search.html',{"message":message,"searched_user": searched_user})

    else:
        message = "You haven't searched for any term"
        return render(request, 'my-instagram/search.html',{"message":message})

@login_required(login_url='/accounts/login/')     
def comment(request,user_id):
    current_user=request.user
    
    image = Image.objects.all()
    if request.method=='POST':
        form=CommentForm(request.POST,request.FILES)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.image=image
            comment.save()
            return redirect('index')
    else:
        form=CommentForm()
    
    return render(request,'my-instagram/comment.html',{"form":form,"image":image})

# def register(request):
#     if request.method =='POST':
#         form=UserCreationForm(request.POST)
#         if form.is_valid():
#             user=form.save()
#             login(request,user)
#             return redirect('registration/login.html')
#     else:
#         form=UserCreationForm()
#     return render(request,'registration/registration_form.html,{'form':form})
                   
