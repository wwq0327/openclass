# -*- coding: utf-8 -*-

import datetime

from django.db import models
from django.core.validators import MaxLengthValidator
from django.contrib.auth.models import User
from tagging.fields import TagField
from tagging.models import Tag

class Project(models.Model):
    CATEGORY_CHOICES = (
        ('1', u'哲学'),
        ('2', u'文学'),
        ('3', u'历史'),
        ('4', u'经济'),
        ('5', u'计算机'),
        ('0', u'其它')
        )

    name = models.CharField(max_length=255)
    creater = models.ForeignKey(User)
    master = models.TextField()
    m_description = models.TextField(validators=[MaxLengthValidator(500)])
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES,
                                null=True, blank=False)
    p_description = models.TextField(validators=[MaxLengthValidator(500)])
    pub_date = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now)
    updated_date = models.DateTimeField(editable=False)
    total = models.IntegerField()
    image = models.ImageField(upload_to="uploads")
    tags = TagField(blank=True)

    class Meta:
        ordering = ['-pub_date']

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        pass

    def _get_tags(self):
        return Tag.objects.get_for_object(self)

    def _set_tags(self, tags):
        return Tag.objects.update_tags(self, tags)

    obj_tags = property(_get_tags, _set_tags)

    def save(self, *args, **kwargs):
        self.updated_date = datetime.datetime.now()

        super(Project, self).save(*args, **kwargs)

class Subject(models.Model):
    project = models.ForeignKey(Project)
    creater = models.ForeignKey(User)
    site = models.URLField()
    pub_date = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now)
    updated_date = models.DateTimeField(editable=False)
    s_num = models.IntegerField()

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return self.site

    def save(self, *args, **kwargs):
        self.updated_date = datetime.datetime.now()

        super(Subject, self).save(*args, **kwargs)
