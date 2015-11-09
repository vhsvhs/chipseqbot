import os
from django.shortcuts import render_to_response
from django.template import RequestContext 
 
def main_page(request):
     return render_to_response( "chipseqbot/index.html", RequestContext(request) )