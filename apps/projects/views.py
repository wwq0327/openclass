# -*- coding: utf-8 -*-

from django.http import Http404, HttpResponseRedirect, HttpResponseForbidden, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.utils import simplejson
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from projects.models import Project, Subject
from projects.forms import ProjectForm, SubjectForm
from people.models import PrjStudy

def index(request):
    projects = Project.objects.all()

    var = RequestContext(request, {'projects': projects})
    return render_to_response('projects/index.html', var)

def project(request, pro_pk):
    project = get_object_or_404(Project, pk=pro_pk)
    subjects = Subject.objects.filter(project=project)

    if request.user.is_authenticated():
        is_join = PrjStudy.objects.filter(projects=project, user=request.user)
    else:
        is_join = False

    var = RequestContext(request, {'project': project,
                                   'subjects': subjects,
                                   'is_join': is_join
                                   })
    return render_to_response('projects/project.html', var)

def subject(request, sub_pk):
    subject = get_object_or_404(Subject, pk=sub_pk)
    if request.user.is_authenticated():
        is_join = PrjStudy.objects.filter(projects=subject.project, user=request.user)
    else:
        is_join = False

    var = RequestContext(request, {'subject': subject,
                                   'is_join': is_join
                                   })

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

@login_required
def prjstudy(request):
    pk = request.GET.get('id')
    prj = Project.objects.get(pk=int(pk))
    user = request.user
    join_s = PrjStudy(projects=prj, user=user)
    join_s.save()

    return HttpResponse("")

@login_required
def un_join(request):
    pk = request.GET.get('id')
    prj = Project.objects.get(pk=int(pk))
    user = request.user
    join_s = PrjStudy.objects.filter(projects=prj, user=user)
    if join_s:
        join_s.delete()

    return HttpResponse("")
