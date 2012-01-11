from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'projects.views.index'),
                       url(r'^project/(?P<pro_pk>\d+)/$', 'projects.views.project', name="pro_detail"),
                       url(r'^subject/(?P<sub_pk>\d+)/$', 'projects.views.subject', name='sub_detail'),
)
