# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from . import models
import datetime

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #触发出错页
    # assert False
    html = "<html><body>offset:%s,dt:%s<body/><html/>"%(offset,dt)
    return HttpResponse(html)


def hello(request):
    return HttpResponse("hello world")


def test(request):
    return HttpResponse("我擦")


def timec(request):
    nowtime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    html = "<html><body>北京时间：%s<body/><html/>"%nowtime
    return HttpResponse(html)

def index(request):
    article = models.Article.objects.get(pk=1)    #pk = 主键  .all 查询所有
    a = {'hello1':article}
    return render(request, 'html_1.html', a)

def index1(request):
    articles = models.Article.objects.all()     #.all 查询所有
    a = {'articles':articles}
    return  render(request,'index1.html', a)

def article_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    a = {'article_page':article}
    return  render(request,'article_page.html',a)



def edit_page(request):
    return render(request,'edit_page.html',)




