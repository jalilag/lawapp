from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^date$',views.today),
  	url(r'^info$',views.chercher_var),
]
