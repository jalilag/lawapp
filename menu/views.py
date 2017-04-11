from django.shortcuts import render,redirect
from .models import Menu, Right_job,Right_member,Right_team
from .forms import form_menu_create, form_right_job,form_right_member, form_right_team
from lib.form import lib_get_field_from_form
from lib.list import build_list_html
from lib.html import libHtml
from .tools import get_valid_menu

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
			return redirect(menu_create)
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
	]}
	}
	content = s.tab_with_fieldset(l1,'tab_form') 
	content = s.form_cadre(request,"right_job",content)
	fields = ['id','menu','job','value','delete']
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




def rights(request,resperpage='10', bloc='1', orderby='menu'):
	s = libHtml()
	form_team = form_right_team(request.POST or None) # Signifie que si le formulaire est retourné invalide il est rechargé avec les erreurs
	form_member = form_right_member(request.POST or None) # Signifie que si le formulaire est retourné invalide il est rechargé avec les erreurs

	l = lib_get_field_from_form(form_member,Right_member)
	l1 = {1: {"Restriction d'accès pour les membres":
	[
		[[l["menu"]['label']],[l['member']['label']]],
		[[l["menu"]['field']],[l['member']['field']]],
		[[s.submit_button("Ok")]]		
	]}}

	ll = lib_get_field_from_form(form_team,Right_team)
	l2 = {1: {"Restriction d'accès pour les équipes":
	[
		[[ll["menu"]['label']],[ll['team']['label']]],
		[[ll["menu"]['field']],[ll['team']['field']]],
		[[s.submit_button("Ok")]]	
	]}}

	content1 = s.tab_with_fieldset(l1,'tab_form')
	content1 += s.input(type="hidden",name="f_name",val="member")
	content1 = s.form_cadre(request,"rights",content1,idkey="form_member")
	content2 = s.tab_with_fieldset(l2,'tab_form') 
	content2 += s.input(type="hidden",name="f_name",val="team")
	content2 = s.form_cadre(request,"rights",content2,idkey="form_team")

	if Right_member.objects.count()>0:
		fields = ['menu','member','delete']
		content1 += build_list_html(request,Right_member,fields,'rights')

	if Right_team.objects.count()>0:
		fields = ['menu','team','delete']
		content2 += build_list_html(request,Right_team,fields,'rights')
	if request.method == 'POST':
		if request.POST["f_name"] == "member":
			if form_member.is_valid():
				form_member.save()
				return redirect(rights)		
			else:
				content1 = l["errors"] + content1
		elif request.POST["f_name"] == "team":
			if form_team.is_valid():
				form_team.save()
				return redirect(rights)		
			else:
				content2 = ll["errors"] + content2

	content1 = s.section("Gestion des droits des membres",content1,'stdsection')
	content2 = s.section("Gestion des droits des équipes",content2,'stdsection')
	content1 = s.container(content1,'div','col-md-4')
	content2 = s.container(content2,'div','col-md-4')
	content = content1+content2
	return render(request, 'gestion/template/form.html', locals())


def generate_menu(request):
	menus = get_valid_menu(request)
	if menus is not None:
		s ='<ul id="menu-accordeon">'
		for i in menus:
			if i.parent == None:
				submenus = get_valid_menu(request,i.id)
				if submenus is not None:
					s += '<li>'
					if i.url is not None:
						s += '<a href="' + i.url + '">'
					else:
						s += '<a href="#">' 
					s += i.title + '</a>'
					s += '<ul>'
					for j in submenus:
						s += '<li>'
						if j.url is not None:
							s += '<a href="' + j.url + '">'
						else:
							s += '<a href="#">' 
						s += j.title + '</a></li>'
					s += '</ul>'
				s += '</li>'
		s += '</ul>'
	else:
		return None
	return s
