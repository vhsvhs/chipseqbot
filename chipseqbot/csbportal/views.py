from django.shortcuts import render

# Create your views here.

def indextest(request):
    return render_to_response("csbportal/index.html",
                              RequestContext(request))
