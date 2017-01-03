from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^info$',views.member_create,name="create"),
]

