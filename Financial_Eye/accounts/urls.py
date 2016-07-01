__author__ = 'fanfan'

from django.conf.urls import url

from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    url(r'^userlist/$', views.UserList.as_view(), name='user_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user detail'),
    #url(r'^adduser/$', views.CreateUser.as_view(), name='add user'),
    url(r'^register/$', views.user_register, name='user register'),
    url(r'^login/$', views.user_login, name='user log in'),

]


urlpatterns = format_suffix_patterns(urlpatterns)