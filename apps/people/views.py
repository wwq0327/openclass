# -*- coding: utf-8 -*-

from django.http import Http404, HttpResponseRedirect, HttpResponseForbidden
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from projects.models import Project, Subject

@login_required
def home(request):

    user = request.user
    projects = user.project_set.all()

    var = RequestContext(request, {'projects': projects})

    return render_to_response('people/home.html', var)
