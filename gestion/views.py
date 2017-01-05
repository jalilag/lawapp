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
	content = l2.titre("Formulaire de création de membre")
	form = form_member_create(request.POST or None) # Signifie que si le formulaire est retourné invalide il est rechargé avec les erreurs
#	content = lib_new_form(request,'create',form.as_p())
	l = lib_get_field_from_form(form,'d')
	l1 = [
	[[l["nom"]["label"]],[l["nom"]["field"]],[l["prenom"]["label"]],[l["prenom"]["field"]]],
	[[l["fonction"]["label"]],[l["fonction"]["field"]]],
	[[l2.submit_button("Envoyé")]]
	]


	content += l2.form_cadre(request,'create',l2.tableau(l1))
	content += form.errors.__str__()
	# Traitement
	if form.is_valid():
		form.save()
		content = 'Votre message est envoyé.'
	return render(request, 'gestion/template/form.html', locals())


def test(request):
	l = libHtml()
	content = l.titre("Titre 1")
	content += l.titre("Titre 3",3)
	a = ["lien1","lien2","lien3"]
	content += l.liste(a)
	a = [
	[["1zerzrez"],["zaezaeza"]],
	[["zezaeza","0","1","2"]],
	[["zaezaeza"], ["azeza"]]
	]
	content += l.tableau(a)
	content += l.submit_button("Bouton")
	return render(request,'base.html', locals())

