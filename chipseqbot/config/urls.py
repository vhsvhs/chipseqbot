from django.conf.urls import patterns, include, url
from django.contrib import admin

#from csbportal import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chipseqbot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^accounts/', include('allauth.urls')),
    #url(r'^indextest/', include(csbportal.views.indextest))
)
