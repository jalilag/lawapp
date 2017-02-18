from django.conf.urls import url
from django.views.generic import ListView
from . import views

urlpatterns = [
    url(r'^member_create$',views.member_create, name='member_create'),
    url(r'''^member_edit(?:\/(?P<member_id>[^/]+))?''',views.member_edit, name='member_edit'),
    url(r'^job_create$',views.job_create, name='job_create'),
    url(r'^team_create$',views.team_create, name='team_create'),
    url(r'''^member_list(?:\/(?P<resperpage>[^/]+))?'''
    				r'''(?:\/(?P<bloc>[^/]+))?'''
                    r'''(?:\/(?P<orderby>[^/]+))?'''
    	,views.member_list, name='member_list'),
 
    url(r'''^member_view(?:\/(?P<id_num>[^/]+))?''',views.member_view, name='member_view'),

    url(r'''^job_list(?:\/(?P<job_id>[^/]+))?'''
                    r'''(?:\/(?P<resperpage>[^/]+))?'''
                    r'''(?:\/(?P<bloc>[^/]+))?'''
                    r'''(?:\/(?P<orderby>[^/]+))?'''
        ,views.job_list, name='job_list'),

    url(r'''^group_list(?:\/(?P<group_id>[^/]+))?'''
                    r'''(?:\/(?P<resperpage>[^/]+))?'''
                    r'''(?:\/(?P<bloc>[^/]+))?'''
                    r'''(?:\/(?P<orderby>[^/]+))?'''
        ,views.group_list, name='group_list'),

]

    # url(r'''^community(?:\/(?P<base_slug>[^/]+))'''
    #                       r'''(?:\/(?P<school_slug>[^/]+))?'''
    #                       r'''(?:\/(?P<grade_slug>[^/]+))?'''
    #                       r'''(?:\/(?P<class_slug>[^/]+))?$''',
    #    'changer.socialschools.communities.views.this_community',
    #    name="community-view"),]

