from django.shortcuts import render
from datetime import datetime

def today(request):
	return render(request,'blog/date.html',{'date':datetime.now()})
# Create your views here.

def chercher_var(request):
	a =5
	b = "rené"
	return render(request,'blog/template/date.html',locals())

def vue_html(request):
	return render(request,'blog/template/index.html',{})
