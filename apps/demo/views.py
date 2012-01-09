# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
    var = RequestContext(request)

    return render_to_response("demo/index.html", var)


def subject(request):
    var = RequestContext(request)

    return render_to_response("demo/subject.html", var)

def project(request):
    var = RequestContext(request)

    return render_to_response("demo/project.html", var)

def create(request):
    var = RequestContext(request)

    return render_to_response("demo/create.html", var)
