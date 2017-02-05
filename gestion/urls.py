from django.conf.urls import url
from django.views.generic import ListView
from . import views

urlpatterns = [
    url(r'^member_create$',views.member_create, name='member_create'),
    url(r'^job_create$',views.job_create, name='job_create'),
    url(r'^team_create$',views.team_create, name='team_create'),
    url(r'''^member_list(?:\/(?P<bloc>[^/]+))?'''
    	r'''(?:\/(?P<orderby>[^/]+))?'''
    	,views.member_list, name='member_list'),
]

    # url(r'''^community(?:\/(?P<base_slug>[^/]+))'''
    #                       r'''(?:\/(?P<school_slug>[^/]+))?'''
    #                       r'''(?:\/(?P<grade_slug>[^/]+))?'''
    #                       r'''(?:\/(?P<class_slug>[^/]+))?$''',
    #    'changer.socialschools.communities.views.this_community',
    #    name="community-view"),]

