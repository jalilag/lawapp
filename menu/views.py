from django.shortcuts import render,redirect
from .models import Menu, Right_job
from .forms import form_menu_create, form_right_job
from lib.form import lib_get_field_from_form
from lib.list import build_list_html
from lib.html import libHtml

def menu_create(request,resperpage='10', bloc='1', orderby='menu'):
	if bloc is None:
		bloc = 1
	if orderby is None:
		orderby = 'id'
	if resperpage is None:
		resperpage = 10

	s = libHtml()
	form = form_menu_create(request.POST or None) # Signifie que si le formulaire est retourné invalide il est rechargé avec les erreurs
	form.fields['parent'].queryset = Menu.objects.filter(parent=None)
	l = lib_get_field_from_form(form,Menu)
	l1 = {1: {'Ajouter un menu':
	[
		[[l["title"]["label"],'stdlab'],[l["title"]["field"],'stdfield']],
		[[l["url"]["label"],'stdlab'],[l["url"]["field"],'stdfield']],
		[[l["parent"]["label"],'stdlab'],[l["parent"]["field"],'stdfield']],	
		[[s.submit_button("Ok")]]
	]}}
	content = s.tab_with_fieldset(l1,'tab_form') 
	content = s.form_cadre(request,"menu_create",content)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
		else:
			content = l["errors"] + content
	if Menu.objects.count()>0:
		obj = Menu.objects.order_by(orderby)
		fields = ['title','parent','url']
		content += build_list_html(request,Menu,fields,'menu_create',[int(resperpage),int(bloc),orderby])

	content = s.section("Creation de menu",content,'stdsection')
	content = s.container(content,'div','col-md-4 col-md-offset-2')

	return render(request, 'gestion/template/form.html', locals())

def right_job(request,resperpage='10', bloc='1', orderby='menu'):
	# Gestion des args
	if bloc is None:
		bloc = 1
	if orderby is None:
		orderby = 'id'
	if resperpage is None:
		resperpage = 10
	s = libHtml()
	form = form_right_job(request.POST or None) # Signifie que si le formulaire est retourné invalide il est rechargé avec les erreurs
	l = lib_get_field_from_form(form,Right_job)
	l1 = {1: {'Gestion des accès':
	[
		[[l["menu"]['label']],[l['job']['label']],[l['value']['label']]],
		[[l["menu"]['field']],[l['job']['field']],[l['value']['field']]],
		[[s.submit_button("Ok")]]		
	]}}
	# l1 = [
	# 	[[l["menu"]['label']],[l['job']['label']],[l['value']['label']]],
	# 	[[l["menu"]['field']],[l['job']['field']],[l['value']['field']]],		
	# ]
	content = s.tab_with_fieldset(l1,'tab_form') 
	# content = s.tableau(l1,'tab_form') + s.submit_button("Ok")
	content = s.form_cadre(request,"right_job",content)
	fields = ['menu','job','value','delete']
	if Right_job.objects.count()>0:
		content += build_list_html(request,Right_job,fields,'right_job',[int(resperpage),int(bloc),orderby])
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect(right_job)
		else:
			content = l["errors"] + content
	content = s.section("Droits associé aux fonctions",content,'stdsection')
	content = s.container(content,'div','col-md-4 col-md-offset-2')
	return render(request, 'gestion/template/form.html', locals())


