# -*- coding: utf-8 -*-
"""DjangoTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from blog import views
from django.contrib import admin

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]



urlpatterns = [

    #url(r'^blog/', include('blog.urls',namespace='blog')),
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', views.hello),
    url(r'^test/$', views.test),
    url(r'^time/$', views.timec),
    url(r"^time/plus/(\d{1,3})$", views.hours_ahead),
    url(r'^index/$', views.index),
    url(r'^index1/$', views.index1),
    # 把匹配到的数字以article_id展示，article_id为函数中需要传递的参数
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    url(r'^edit/$', views.edit_page),

]


