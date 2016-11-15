# -*- coding:utf-8 -*-
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


class Photo(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos')
    description = models.TextField(blank=True)
    words = models.TextField(blank=True)
    username = models.ForeignKey(User)

    class Meta:
        ordering = ('title',)
    #  以title排序

    def __str__(self):
        return self.title
    #  一个Photo对象的显示名称
'''
    @models.permalink
    def get_absolute_url(self):
        return 'photo_detail', None, {'object_id': self.id}
'''

admin.site.register(Photo)
#  如果希望在django自带的admin模型中出现我们定义的Photo模型，这里需要注册一下