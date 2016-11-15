# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from studio.models import Photo


def sign_up(request):
    errors = []
    username = None
    password = None
    if request.method == 'POST':
        if request.POST.get('username'):
            username = request.POST.get('username')
        else:
            errors.append('输入用户名')
        if request.POST.get('password'):
            password = request.POST.get('password')
        else:
            errors.append('请输入密码')
        user = authenticate(username=username, password=password)
        if username and password:
            if user:
                if user.is_active:
                    photos = Photo.objects.all()
                    login(request, user)
                    return render_to_response('homeIndex.html', {'photos': photos, 'name': user})  # 登录成功后
                else:
                    errors.append('你被禁止登陆了')
            else:
                errors.append('没找到这个用户 o(︶︿︶)o ')
    return render_to_response('sign_up.html', {'errors': errors}, context_instance=RequestContext(request))


def sign_in(request):
    username = None
    password = None
    password2 = None
    errors = []
    if request.method == 'POST':
        if request.POST.get('username'):
            username = request.POST.get('username')
        else:
            errors.append('注册要有一个用户名')
        if request.POST.get('password'):
            password = request.POST.get('password')
        else:
            errors.append('需要一个密码')
        if request.POST.get('password2'):
            password2 = request.POST.get('password2')
        else:
            errors.append('两次密码不一样')

        if not User.objects.filter(username=username):  # 判断用户名是否已被注册
            if password == password2:
                user = authenticate(username=username, password=password)
                if user:
                    errors.append('你已经注册过了，直接登录吧~')
                else:
                    user = User.objects.create_user(username=username, password=password)
                    user.is_active = True
                    user.save()
                    return HttpResponseRedirect('/signup')  # 系统会优先在本app下的template目录里面找
            else:
                errors.append('两次密码要一样才能注册喔')
        else:
            errors.append('请换个用户名')
    return render_to_response('sign_in.html', {'errors': errors}, context_instance=RequestContext(request))


def sign_out(request):
    logout(request)
    return HttpResponseRedirect('/home/index')
