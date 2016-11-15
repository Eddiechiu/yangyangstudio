# -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from studio.views import home, index, detail 
from register.views import sign_up, sign_in, sign_out
from upload.views import upload

urlpatterns = patterns('',
                       url(r'^$', home),
                       url(r'^home/index/$', index),
                       url(r'^home/detail/$', detail),
                       url(r'^home/upload/$', upload),
                       #  直接用'studio.views.index'绝对地址，可以减少前面import的数量，看起来也更直观
                       
                       url(r'^admin/', admin.site.urls),
                       url(r'^signup/$', sign_up),
                       url(r'^signin/$', sign_in),
                       url(r'^home/index/sign_out', sign_out),
                       url(r'^comments/', include('django_comments.urls')),
                       #  ^online/是online这个app的一级地址，include功能可以跳转至online下的urls.py，里面包含了二级地址
                       #  同时要注意，如果一个地址后面还有地址，在正则表达式的最后不能以$结束，否则不会找二级地址
                       #  尝试把每个app的地址都打包，再用include写一遍
                       )+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#  加入static(...)为每一个用户上传的静态文件添加地址
