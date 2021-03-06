from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       #url(r'', include('demo.urls')),
                       url(r'', include('projects.urls')),
                       url(r'', include('people.urls')),
                       url(r'^accounts/', include('registration.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'comments/', include('django.contrib.comments.urls')),
                       url(r'^help/$', include('help.urls')),
)

media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
urlpatterns += patterns('',
                        (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
                         {
                             'document_root': settings.MEDIA_ROOT,
                             }),
                        )
