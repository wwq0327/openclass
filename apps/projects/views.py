# -*- coding: utf-8 -*-

from django.http import Http404, HttpResponseRedirect, HttpResponseForbidden
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

from projects.models import Project, Subject

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
