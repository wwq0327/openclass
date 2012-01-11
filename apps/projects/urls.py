from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'projects.views.index'),
                       url(r'^project/(?P<pro_pk>\d+)/$', 'projects.views.project', name="pro_detail"),
                       url(r'^subject/(?P<sub_pk>\d+)/$', 'projects.views.subject', name='sub_detail'),
                       url(r'^project/create/$', 'projects.views.prj_create'),
                       url(r'^project/(?P<prj_pk>\d+)/create/$', 'projects.views.subj_create'),
                       url(r'^project/prj_s/(?P<prj_pk>\d+)/$', 'projects.views.prjstudy'),
)
