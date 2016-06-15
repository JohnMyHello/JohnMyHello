#-*- coding=utf-8 -*-
from django.conf.urls import url
from blog.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^archive/$', archive, name='archive'),
    url(r'^article/$', article, name='article'),  #文章详情页
    url(r'^comment/post/$', comment_post, name='comment_post'), #提交评论
    url(r'^logout$', do_logout, name='logout'), #注销
    url(r'^reg$', do_reg, name='reg'),  #注册
    url(r'^login$', do_login, name='login'),    #登陆
    url(r'^category$', category, name='category$'),
]
