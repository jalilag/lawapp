"""lawapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views
#from .views import list_links

urlpatterns = [
    url(r'^admin/', admin.site.urls),
#    url(r'^$', list_links),
#    url(r'^blog/',include('blog.urls')),
    url(r'^gestion/',include('gestion.urls')),
    url(r'^menu/',include('menu.urls')),
    url(r'^home/',include('home.urls')),
    url(r'^ajax_list_delete/$',views.ajax_list_delete,name="ajax_list_delete"),
    url(r'^ajax_list_delete_process/$',views.ajax_list_delete_process,name="ajax_list_delete_process"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
