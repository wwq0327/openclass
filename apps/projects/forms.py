# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User

from projects.models import Project, Subject

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['creater', 'pub_date', 'updated_date']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        exclude = ['project', 'creater', 'pub_date', 'updated_date']

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

