from django.conf.urls import patterns, include, url
from django.contrib import admin
from quadratic import views

urlpatterns = patterns('',
    # quadratic
    url(r'^results/', views.quadratic_results, name='quadratic_results'),
)