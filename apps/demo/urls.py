from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'demo.views.index'),
                       url(r'^subject/$', 'demo.views.subject'),
                       url(r'^project/$', 'demo.views.project'),
                       url(r'^project/create/$', 'demo.views.create'),
                       url(r'^home/$', 'demo.views.home'),
)
