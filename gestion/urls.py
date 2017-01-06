from django.conf.urls import url
from django.views.generic import ListView
from . import views

urlpatterns = [
    url(r'^info$',views.member_create,name="create"),
]
