# -*- coding: utf-8 -*-

import datetime

from django.db import models
from django.contrib.auth.models import User

from projects.models import Project

class PrjStudy(models.Model):
    project = models.ForeignKey(Project)
    user = models.ForeignKey(User)
    join_date = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now)

    class Meta:
        ordering = ['-join_date']

    def __unicode__(self):
        return '%s %s' % (self.user, self.project)

    @models.permalink
    def get_absolute_url(self):
        return self.project.get_absolute_url()

    def save(self, *args, **kwargs):
        """
        todo: 如何才能只保存一次数据
        """
        ## if not self.pk:
        ##     self.join_date = datetime.datetime.now()

        super(PrjStudy, self).save(*args, **kwargs)

