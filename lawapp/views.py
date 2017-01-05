from django.shortcuts import render,redirect,reverse
from django.core.urlresolvers import get_resolver
from gestion import views as v1
from lib.url import lib_get_all_urls
from lib.html import libHtml

def list_links(request):
	l = lib_get_all_urls()
	l1 = list()
	l2 = libHtml()
	for i in l:
		l1.append(l2.lien(i,i))
	l1.sort()
	content = l2.liste(l1)
	return render(request,"base.html",locals())
