# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User

from projects.models import Project, Subject

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['creater', 'pub_date', 'updated_date', 'total']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        exclude = ['project', 'creater', 'pub_date', 'updated_date']
