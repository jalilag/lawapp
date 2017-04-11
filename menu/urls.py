from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'''^menu_create(?:\/(?P<resperpage>[^/]+))?'''
    				r'''(?:\/(?P<bloc>[^/]+))?'''
                    r'''(?:\/(?P<orderby>[^/]+))?'''
                    ,views.menu_create, name='menu_create'),
	url(r'''^right_job(?:\/(?P<resperpage>[^/]+))?'''
    				r'''(?:\/(?P<bloc>[^/]+))?'''
                    r'''(?:\/(?P<orderby>[^/]+))?'''
                    ,views.right_job, name='right_job'),
    url(r'''^rights(?:\/(?P<resperpage>[^/]+))?'''
                    r'''(?:\/(?P<bloc>[^/]+))?'''
                    r'''(?:\/(?P<orderby>[^/]+))?'''
                    ,views.rights, name='rights'),
]
