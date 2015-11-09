from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chipseqbot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^csbportal/', include('csbportal.urls')),
    url(r'^$', views.main_page),
)
