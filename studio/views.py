# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from studio.models import Photo
from django.template import RequestContext
from django.http import HttpResponse


def home(request):
    return render_to_response('home.html')


def index(request):
    photos = Photo.objects.all()
    user = ''
    if request.user.is_authenticated():
        user = request.user.get_username()
    return render_to_response('homeIndex.html', {'photos': photos, 'name': user}, context_instance=RequestContext(request))


def detail(request):
    user = ''
    if request.user.is_authenticated():
        user = request.user.get_username()
    photo_name = request.GET['photo_name']
    photo = Photo.objects.filter(title=photo_name)
    photo = photo[0]
    return render_to_response('detail.html', {'photo': photo, 'name': user}, context_instance=RequestContext(request))
