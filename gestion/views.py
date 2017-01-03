from django.shortcuts import render,redirect
from .forms import form_member_create
from .models import member, fonction
from lib.form import lib_new_form, lib_get_field_from_form,lib_gen_table_from_list

def member_create(request):
	"""
		Vue d'édition et de création des membres
	"""
	form = form_member_create(request.POST or None) # Signifie que si le formulaire est retourné invalide il est rechargé avec les erreurs
#	content = lib_new_form(request,'create',form.as_p())
	l = lib_get_field_from_form(form,'d')
	l1 = [
	[[l["nom"]["label"]],[l["nom"]["field"]],[l["prenom"]["label"]],[l["prenom"]["field"]]],
	[[l["fonction"]["label"]],[l["fonction"]["field"]]],
	[[l["submit"]["field"]]]
	]
	content = lib_new_form(request,'create',lib_gen_table_from_list(l1),False)
	# Traitement
	if form.is_valid():
		form.save()
		content = 'Votre message est envoyé.'
	return render(request, 'gestion/template/form.html', locals())