from django.shortcuts import render,redirect,reverse
from django.views.generic import ListView
from .forms import form_member_create, form_job_create, form_team_create
from lib.form import lib_get_field_from_form
from lib.html import libHtml
from lib.list import build_list_html
from .models import Member

def member_create(request):
	"""
		Vue d'édition et de création des membres
	"""
	l2 = libHtml()
	form = form_member_create(request.POST or None,request.FILES) # Signifie que si le formulaire est retourné invalide il est rechargé avec les erreurs

	l = lib_get_field_from_form(form,'d')
	l1 = [
	[[l["firstname"]["label"]],[l["firstname"]["field"]],[l["lastname"]["label"]],[l["lastname"]["field"]]],
	[[l["job"]["label"]],[l["job"]["field"]]],
	[[l["team"]["label"]],[l["team"]["field"]]],
	[[l["photo"]["label"]],[l["photo"]["field"]]],
	[[l2.submit_button("Envoyé")]],
	]

	# Formation du formulaire
	content = l2.form_set_all(request,"member_create",l2.tableau(l1),form,"azeazea",True)
	# content = l2.form_set_all(request,"create",form.as_table(),None,"azeazea")

	if form.is_valid():
		form.save()
		# Génération de la page en cas de réussite
		content = 'Votre message est envoyé.'
		
	return render(request, 'gestion/template/form.html', locals())


def job_create(request):
	"""
		Vue création des jobs
	"""
	l2 = libHtml()
	form = form_job_create(request.POST or None) # Signifie que si le formulaire est retourné invalide il est rechargé avec les erreurs
	l = lib_get_field_from_form(form,'d')
	l1 = [
	[[l["title"]["label"]],[l["title"]["field"]]],
	[[l2.submit_button("Envoyé")]],
	]

	content = l2.form_set_all(request,"job_create",l2.tableau(l1),form,"eaeaz")	

	if form.is_valid():
		form.save()
		# Génération de la page en cas de réussite
		content = 'Votre message est envoyé.'
		
	return render(request, 'gestion/template/form.html', locals())

def team_create(request):
	"""
		Vue création des jobs
	"""
	l2 = libHtml()
	form = form_team_create(request.POST or None) # Signifie que si le formulaire est retourné invalide il est rechargé avec les erreurs
	l = lib_get_field_from_form(form,'d')
	l1 = [
	[[l["title"]["label"]],[l["title"]["field"]]],
	[[l2.submit_button("Envoyé")]],
	]

	content = l2.form_set_all(request,"team_create",l2.tableau(l1),form,"eaeaz")	

	if form.is_valid():
		form.save()
		# Génération de la page en cas de réussite
		content = 'Votre message est envoyé.'
		
	return render(request, 'gestion/template/form.html', locals())

def member_list(request, bloc='1', orderby='id'):
	if bloc is None:
		bloc = '1'
	if orderby is None:
		orderby = 'id'
	resperpage = 10
	fields = ['id','firstname','lastname','job','photo']
	content = build_list_html(Member,fields,'member_list',resperpage,int(bloc),orderby)
	return render(request, 'gestion/template/form.html', locals())