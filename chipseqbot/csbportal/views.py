import os
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.

def indextest(request):
    return render_to_response("csbportal/index.html",
                              RequestContext(request))
