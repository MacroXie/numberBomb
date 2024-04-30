# -*- coding = utf-8 -*-
# @Time : 2023/6/9 8:32
# @Author : tqy
# @File : urls.py.py
# @Software : PyCharm

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='registration'),
    path('result', views.result, name='result'),
    path('control', views.admin, name='control'),
    path('board', views.board, name='board')
]
