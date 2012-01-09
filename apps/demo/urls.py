from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'demo.views.index'),
                       url(r'^subject/$', 'demo.views.subject'),
)
