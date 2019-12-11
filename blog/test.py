#coding=utf-8
import os,django,datetime
# from django import template

#指定配置文件
from django.template import Template,Context
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoTest.settings")
django.setup()


#例子1
t = Template('我的名字是 : {{ name }}.')
a = Template('我的名字是 : {{ abc }}.')
print t
c = Context({'name':'袁猛','abc':'def'})
print (t.render(c))
print (a.render(c))


#日期组合
d = datetime.date(2019,4,2)
print d
# #

#判断
# if False:
#     print ('111111111')
# else:
#     print ('2222222')
#
# if True:
#     print ('1111111111')
# else:
#     print ('222222222')


#例子2
# html = """
# <p>{{ name1 }}你好:<p/>
# <p>我叫{{ name2 }}，来自{{ city }},工作地点{{ work }}<p/>
# {% if exptct %}
# <p>你是谁？<p/>
# {% else %}
# <p>我是谁？<p/>
# {% endif %}
# <p>{{ name2 }}<br/>{{ nowtime }}<p/>
# <p>{{ now_time|date:'F J, Y' }}<p/>
# <li>{{ text }}<li/>
# """
# E = Template(html)
# texts = ('a1','b1','c1','d1','e1','f1','g1')
# for text in texts:
#     F = Context({
#         'name1':'王老板',
#         'name2':'袁猛',
#         'city':'荆州',
#         'work':'福田八卦岭',
#         'exptct':True,
#         'nowtime':datetime.datetime.now(),
#         'now_time':datetime.date(2009, 4, 2),
#         'text':text
#     })
#     print (E.render(F))


#调用数组数据
# data = {'name':'yuanm','age':'18'}
# html1 = """
# my name is {{ data1.name }},year{{ data1.age }}
# """
# H = Template(html1)
# I = Context({
#     'data1':data
# })
# print (H.render(I))


#单独打印年月日
# J = datetime.datetime.now()
# print (J.year,J.day,J.month)


#冒泡排序
# lis = [12,45,3,78,24,56,1,19,99,54]
# print (lis)
# def aa(lis):
#     for i in range(0,len(lis)):
#         for j in range(i+1,len(lis)):
#             if lis[i]>lis[j]:
#                 lis[i],lis[j] = lis[j],lis[i]
#     return lis
# print (aa(lis))


#if判断 ifequal  ifnotequal
# html = """
# {% ifequal A B %}
# <p>相等1<p/>
# {% else %}
# <p>不相等1<p/>
# {% endifequal%}
# {% ifnotequal A B %}
# <p>不相等2<p/>
# {% else %}
# <p>相等2<p/>
# {% endifnotequal %}
# """
# E = Template(html)
# F = Context({
#     "A":1,
#     "B":2
# })
# print (E.render(F))


#for循环列表判断
# html = """
# {% for A in list1 %}
# <p>{{A}}<p/>
# {%endfor%}
# """
# list2 = [12,45,3,78,24,56,1,19,99,54]
# E = Template(html)
# F = Context({
#     "list1":list2
# })
# print (E.render(F))


#for循环数组判断
# html = """
# {% for B in tup.keys %}
# <p>打印键：{{B}}<p/>
# {%endfor%}
# {% for B in tup.values %}
# <p>打印值：{{B}}<p/>
# {%endfor%}
# """
# tup1 = {"name":"袁猛","age":"18"}
# E = Template(html)
# F = Context({
#     "tup":tup1
# })
# print (E.render(F))

