from django.conf.urls import patterns, url
from students.views import StudentDeleteView, StudentListView, StudentDelailView, StudentCreateView, StudentUpdateView

urlpatterns = patterns('',
	url(r'^(?P<pk>\d+)/$', StudentDelailView.as_view(), name='detail'),
    url(r'^$', StudentListView.as_view(), name='list_view'),
    url(r'^add/$', StudentCreateView.as_view(), name='add'),
    url(r'^edit/(?P<pk>\d+)/$', StudentUpdateView.as_view(), name='edit'),
    url(r'^remove/(?P<pk>\d+)/$', StudentDeleteView.as_view(), name='remove'),
    )