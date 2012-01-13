# -*- coding: utf-8 -*-

import markdown

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.shortcuts import render_to_response, get_object_or_404

def help(request):
    tmp = get_template("help/help.md")
    help_content = tmp.render(Context({}))
    md = markdown.markdown(help_content)

    var = RequestContext(request, {'md': md})

    return render_to_response('help/help.html', var)
