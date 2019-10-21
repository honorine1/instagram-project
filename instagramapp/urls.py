from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
url(r'^$',views.index,name='index'),
url(r'^posts/', views.posts, name='posts'),
url(r'^new/post/$', views.new_post, name='new_post'),
url(r'^new/post/postsToday/',views.posts_today,name='postsToday'),
url(r'^profile/(\d+)',views.profile,name = 'profile'),
url(r'^updateProfile',views.updateProfile,name = 'updateProfile'),
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)