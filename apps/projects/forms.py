# -*- coding: utf-8 -*-

from django.conf import settings
from django import forms
from django.contrib.auth.models import User

from projects.models import Project, Subject

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['creater', 'pub_date', 'updated_date']

    def clean_image(self):
        if self.cleaned_data['image'].size > settings.MAX_IMAGE_SIZE:
            max_size = settings.MAX_IMAGE_SIZE / 1024
            ms = ""
        return self.cleaned_data['image']

    def save(self, user):
        name = self.cleaned_data['name']
        master = self.cleaned_data['master']
        m_description = self.cleaned_data['m_description']
        category = self.cleaned_data['category']
        p_description = self.cleaned_data['p_description']
        total = self.cleaned_data['total']
        image = self.cleaned_data['image']
        tags = self.cleaned_data['tags']

        model = Project(name=name,
                        creater=user,
                        master=master,
                        m_description=m_description,
                        category=category,
                        p_description=p_description,
                        total=total,
                        image=image,
                        tags=tags)
        model.save()

        return model

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        #exclude = ['project', 'creater', 'pub_date', 'updated_date']
        fields = ('name', 'site', 's_num',)

    def save(self, user, project):
        name = self.cleaned_data['name']
        site = self.cleaned_data['site']
        s_num = self.cleaned_data['s_num']

        model = Subject(project=project,
                        name=name,
                        creater=user,
                        site=site,
                        s_num=s_num)
        model.save()
        return model


