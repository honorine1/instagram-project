# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'my-instagram/index.html')

# def current_post:
#     return render(request,'my-instagram/current_post.html')from django.contrib.auth.decorators import login_required.

#.......
# 
# @login_required(login_url='/accounts/login/')
# def article(request, article_id):