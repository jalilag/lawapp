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
	# Formation du formulaire
	content = l2.form_set_all(request,"create",l2.tableau(l1),form,"azeazea")
	# content = l2.form_set_all(request,"create",form.as_table(),None,"azeazea")

	if form.is_valid():
		form.save()
		# Génération de la page en cas de réussite
		content = 'Votre message est envoyé.'
		
	return render(request, 'gestion/template/form.html', locals())



