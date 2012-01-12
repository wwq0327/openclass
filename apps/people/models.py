# -*- coding: utf-8 -*-

import datetime

from django.db import models
from django.contrib.auth.models import User

from projects.models import Project

class PrjStudy(models.Model):
    projects = models.ForeignKey(Project)
    user = models.ForeignKey(User)
    join_date = models.DateTimeField(editable=False)

    class Meta:
        ordering = ['-join_date']

    def __unicode__(self):
        return '%s %s' % (self.user, self.projects)

    @models.permalink
    def get_absolute_url(self):
        return self.projects.get_absolute_url()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.join_date = datetime.datetime.now()
        super(PrjStudy, self).save(*args, **kwargs)

