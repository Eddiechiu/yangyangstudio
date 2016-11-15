# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from studio.models import Photo
from PIL import Image
from django import forms
from django.template import RequestContext
from django.http import HttpResponseRedirect


class ImageForm(forms.Form):
    image = forms.ImageField()


def upload(request):
    errors = []
    if not request.user.is_authenticated():
        errors.append('请先登录，再上传喔')
    else:
        user = request.user
        image_upload = None
        if request.method == 'POST':
            try:
                image_upload = request.FILES['image_file']
            except:
                pass
            if not image_upload:
                errors.append('请选择要上传的图片')

            title = request.POST.get('title_file')
            if not title:
                errors.append('请为图片写一个标题')

            description = request.POST.get('text_file')
            if not description:
                errors.append('请写一些描述~')

            if image_upload and title and description:
                Photo.objects.create(username=user, image=image_upload, title=title, description=description)
                # 这里create的Photo实例，其中根据studio.models.Photo中的定义，username是一个User实例（这是一个命名失误。。。）
                image_upload.close()
                return HttpResponseRedirect('/home/index')  # 需要重定向，否则用户刷新页面会重复提交form

    return render_to_response('upload.html', {'errors': errors}, context_instance=RequestContext(request))
