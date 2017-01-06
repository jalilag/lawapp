from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .forms import form_member_create
from .models import member, fonction
from lib.form import lib_get_field_from_form
from lib.html import libHtml

def member_create(request):
	"""
		Vue d'édition et de création des membres
	"""
	l2 = libHtml()	
	form = form_member_create(request.POST or None) # Signifie que si le formulaire est retourné invalide il est rechargé avec les erreurs
	l = lib_get_field_from_form(form,'d')
	l1 = [
	[[l["nom"]["label"]],[l["nom"]["field"]],[l["prenom"]["label"]],[l["prenom"]["field"]]],
	[[l["fonction"]["label"]],[l["fonction"]["field"]]],
	[[l2.submit_button("Envoyé")]]
	]

	content = l2.form_cadre(request,'create',l2.tableau(l1))
	content = l2.div(content, "col-lg-4")
	if form.errors.__str__() != "":
		content += l2.div(form.errors.__str__(),"col-lg-4")
	# Traitement
	content = l2.titre("Formulaire de création de membre")+content

	content = l2.div(content, "container")
	if form.is_valid():
		form.save()
		content = 'Votre message est envoyé.'
	return render(request, 'gestion/template/form.html', locals())



