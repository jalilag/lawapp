from django.shortcuts import render
from datetime import datetime
from django.views.generic import TemplateView

def today(request):
	return render(request,'blog/date.html',{'date':datetime.now()})
# Create your views here.

def chercher_var(request):
	a =5
	b = "rené"
	return render(request,'blog/template/date.html',locals())

def vue_html(request):
	return render(request,'blog/template/index.html',{})

def vue2(request):
	content = "<h1>Titre 1</h1>"
	return render(request,'test.html',locals())
