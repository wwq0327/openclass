# -*- coding: utf-8 -*-

from django.http import Http404, HttpResponseRedirect, HttpResponseForbidden
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

from projects.models import Project, Subject

def project(request, pro_pk):
    pass
