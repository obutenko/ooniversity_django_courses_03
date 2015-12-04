from django.conf.urls import patterns, url

from courses.views import detail, add, edit, remove, add_lesson

urlpatterns = patterns('',

                       url(r'^(?P<course_id>\d+)/$', detail, name='detail'),
                       url(r'^add/$', add, name='add'),
                       url(r'^edit/(?P<course_id>\d+)/$', edit, name='edit'),
                       url(r'^remove/(?P<course_id>\d+)/$', remove, name='remove'),
                       url(r'^(?P<course_id>\d+)/add_lesson/$', add_lesson, name='add-lesson'),



                       )
