# -*- coding: utf-8 -*-

from django.http import Http404, HttpResponseRedirect, HttpResponseForbidden
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

from projects.models import Project, Subject
from projects.forms import ProjectForm, SubjectForm

def index(request):
    projects = Project.objects.all()

    var = RequestContext(request, {'projects': projects})
    return render_to_response('projects/index.html', var)

def project(request, pro_pk):
    project = get_object_or_404(Project, pk=pro_pk)
    subjects = Subject.objects.filter(project=project)

    var = RequestContext(request, {'project': project,
                                   'subjects': subjects
                                   })
    return render_to_response('projects/project.html', var)

def subject(request, sub_pk):
    subject = get_object_or_404(Subject, pk=sub_pk)

    var = RequestContext(request, {'subject': subject})

    return render_to_response('projects/subject.html', var)

def prj_create(request):

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            prj = form.save(user=request.user)
            return HttpResponseRedirect(prj.get_absolute_url())
    else:
        form = ProjectForm()

    var = RequestContext(request, {'form': form})
    return render_to_response('projects/prj_create.html', var)

def subj_create(request, prj_pk):
    prj = get_object_or_404(Project, pk=prj_pk)

    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            sub = form.save(user=request.user, project=prj)
            return HttpResponseRedirect(sub.project.get_absolute_url())
    else:
        form = SubjectForm()

    var = RequestContext(request, {'form': form})

    return render_to_response('projects/subj_create.html', var)
