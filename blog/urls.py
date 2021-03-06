from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
   
    url(r'^$', views.post_list, name='post_list'),
    url('post/(?P<pk>\d+)/$', views.post_details, name='post_details'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]