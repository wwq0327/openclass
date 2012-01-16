# -*- coding: utf-8 -*-

import datetime

from django.db import models
from django.core.validators import MaxLengthValidator
from django.contrib.auth.models import User
from tagging.fields import TagField
from tagging.models import Tag

from utils import get_partition_id, safe_filename
from storage import ImageStorage

## def determine_image_upload_path(instance, filename):
##     return "uploads/%(partition)d_%(filename)s" % {
##         'partition': get_partition_id(instance.pk),
##         'filename': safe_filename(filename),
##         }


def determine_image_upload_path(instance, filename):
    return "uploads/%(filename)s" % {
        ## 'partition': get_partition_id(instance.pk),
        'filename': safe_filename(filename),
        }

class Project(models.Model):
    CATEGORY_CHOICES = (
        ('1', u'哲学'),
        ('2', u'文学'),
        ('3', u'历史'),
        ('4', u'经济'),
        ('5', u'计算机'),
        ('6', u'物理'),
        ('0', u'其它')
        )

    name = models.CharField(u'课题名称', max_length=255)
    creater = models.ForeignKey(User)
    master = models.CharField(u'讲师', max_length=60, blank=True)
    m_description = models.TextField(u'讲师简介', validators=[MaxLengthValidator(500)], help_text=u"关于讲师的一些简明介绍")
    category = models.CharField(u'分类', max_length=30, choices=CATEGORY_CHOICES,
                                null=True, blank=True)
    p_description = models.TextField(u'课程简介', validators=[MaxLengthValidator(500)])
    pub_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    total = models.IntegerField(u'总课时数')
    image = models.ImageField(u'图片', upload_to=determine_image_upload_path, storage=ImageStorage(), blank=True, null=True)

    tags = TagField(u'标签', blank=True, help_text=u"给本课程打上标签，标签间请用空间分隔")

    class Meta:
        ordering = ['-pub_date']

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('pro_detail', (), {
            'pro_pk': self.pk })

    def _get_tags(self):
        return Tag.objects.get_for_object(self)

    def _set_tags(self, tags):
        return Tag.objects.update_tags(self, tags)

    obj_tags = property(_get_tags, _set_tags)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.pub_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()

        super(Project, self).save(*args, **kwargs)

class Subject(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(u'课名', max_length=255)
    creater = models.ForeignKey(User)
    site = models.URLField(u'视频地址')
    pub_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    s_num = models.IntegerField(u'课时序号')

    class Meta:
        ordering = ['s_num']

    def __unicode__(self):
        return self.site

    def save(self, *args, **kwargs):
        if not self.pk:
            self.pub_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()

        super(Subject, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('sub_detail', (), {
            'sub_pk': self.pk})
