import os
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

@login_required
def indextest(request):
    return render_to_response("csbportal/index.html", RequestContext(request))
