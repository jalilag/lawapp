from django.shortcuts import render, redirect,reverse,get_object_or_404
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.views.generic import ListView
from .forms import form_member_create, form_member_edit, form_job_create, form_team_create
from lib.form import lib_get_field_from_form
from lib.html import libHtml
from lib.list import build_list_html
from lib.model import get_verbose
from .models import Member,Job, Team
from lawapp.settings import MEDIA_URL

def member_create(request):
	"""
		Vue d'édition et de création des membres
	"""
	l2 = libHtml()
	form = form_member_create(request.POST or None,request.FILES) # Signifie que si le formulaire est retourné invalide il est rechargé avec les erreurs
	l = lib_get_field_from_form(form)

	l1 = [
	[[l["firstname"]["label"]],[l["firstname"]["field"]],[l["lastname"]["label"]],[l["lastname"]["field"]]],
	[[l["job"]["label"]],[l["job"]["field"]]],
	[[l["team"]["label"]],[l["team"]["field"]]],
	[[l["photo"]["label"]],[l["photo"]["field"]]],
	[[l2.submit_button("Envoyé")]],
	]

	# Formation du formulaire
	content = l2.form_cadre(request,"member_create",l2.tableau(l1),True)
	# content = l2.form_set_all(request,"create",form.as_table(),None,"azeazea")
	content = l2.section('Création de membre',content)
	content = l2.container(content,'div','col-md-6 col-md-offset-3')

	if form.is_valid():
		form.save()
		return redirect('member_list')		
		# Génération de la page en cas de réussite
	return render(request, 'gestion/template/form.html', locals())


def member_edit(request,member_id):
	obj = get_object_or_404(Member,pk=member_id)
	if request.method == 'POST':
		form = form_member_edit(request.POST or None,request.FILES,instance=obj) # Signifie que si le formulaire est retourné invalide il est rechargé avec les erreurs
	else:
		form = form_member_edit(instance=obj) # Signifie que si le formulaire est retourné invalide il est rechargé avec les erreurs
	l = lib_get_field_from_form(form)
	l2 = libHtml()

	l1 = [
	[[l["firstname"]["label"]],[l["firstname"]["field"]],[l["lastname"]["label"]],[l["lastname"]["field"]]],
	[[l["job"]["label"]],[l["job"]["field"]]],
	[[l["team"]["label"]],[l["team"]["field"]]],
	[[l["photo"]["label"]],[l["photo"]["field"]]],
	[[l2.submit_button("Envoyé")]],
	]
	if 'errors' in l:
		print(l['errors'])
	# Formation du formulaire
	content = l2.form_cadre(request,"member_edit",l2.tableau(l1),True,arg=[member_id])
	# content = l2.form_cadre(request,"member_edit",form.as_p(),True,arg=[member_id])
	content = l2.section('Edition de membre',content)
	content = l2.container(content,'div','col-md-6 col-md-offset-3')

	if form.is_valid():
		form.save()
		return redirect('member_view',member_id)
		# Génération de la page en cas de réussite
	return render(request, 'gestion/template/form.html', locals())

def member_list(request,resperpage='10', bloc='1', orderby='id' ):
	# Gestion des args
	if bloc is None:
		bloc = 1
	if orderby is None:
		orderby = 'id'
	if resperpage is None:
		resperpage = 10
	# En cas de suppression
	if len(request.POST) > 0 and 'delete' in request.POST:
		l = dict(request.POST)
		for i in l['delete']:
			o = get_object_or_404(Member, pk=int(i))
			o.delete()
		redirect('member_list')
	# Fields à afficher
	fields = ['id','firstname','lastname','job','team','photo','delete']
	# Génération de la liste
	l2 = libHtml()
	obj = Member.objects.order_by(orderby)
	content = build_list_html(Member,obj,fields,'member_list',[int(resperpage),int(bloc),orderby],'member_view')
	if 'delete' in fields:
		content = l2.form_cadre(request,'member_list',content,name='form_delete',option='onsubmit="return check_del();"')
	content = l2.section('Liste des membres',content)
	content = l2.container(content,'div','col-md-8 col-md-offset-2')
	return render(request, 'gestion/template/form.html', locals())

def member_view(request,id_num):
	o = get_object_or_404(Member,pk=int(id_num))
	go = o.team.all()
	Ngo = len(go)
	l2 = libHtml()
	s = ""
	for i in range(0,Ngo):
		ggo = get_object_or_404(Team,title=str(go[i]))
		s += l2.lien(str(go[i]),reverse('group_list',args=[str(ggo.pk)]))
		if i < Ngo-1:
			s += ', '

	tab = [
	[[l2.button(' Edit',reverse('member_edit',args=[id_num]),'info','wrench'),'class="left"']],
	[[get_verbose(o,'firstname') + " : ",'class="bbigField"'],[o.firstname,'class="bigField"']],
	[[get_verbose(o,'lastname') + " : ",'class="bbigField"'],[o.lastname,'class="bigField"']],
	[[get_verbose(o,'job') + " : ",'class="bbigField"'],[l2.lien(str(o.job),reverse('job_list',args=[o.job.pk])),'class="bigField"']],
	[[get_verbose(o,'team') + " : ",'class="bbigField"'],[s,'class="bigField"']],
	]
	tabh = [
	[[l2.tableau(tab,None,False)],[l2.photo_display(MEDIA_URL+str(o.__getattribute__('photo')),None,'200'),'class="right"']]
	]

	content = l2.section(o.firstname + " " + o.lastname,l2.tableau(tabh,'wide',False))
	content = l2.container(content,'div','col-md-6 col-md-offset-3')
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
	content = l2.form_cadre(request,"job_create",l2.tableau(l1))	
	content = l2.section('Création des profils',content)
	content = l2.container(content,'div','col-md-6 col-md-offset-3')
	if form.is_valid():
		form.save()
		# Génération de la page en cas de réussite
		return redirect('member_list')				
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

	content = l2.form_cadre(request,"team_create",l2.tableau(l1))	
	content = l2.section('Création des équipes',content)
	content = l2.container(content,'div','col-md-6 col-md-offset-3')

	if form.is_valid():
		form.save()
		# Génération de la page en cas de réussite
		return redirect('member_list')		
		
	return render(request, 'gestion/template/form.html', locals())


def job_list(request,job_id,resperpage='10',bloc='1', orderby='id' ):
	if bloc is None:
		bloc = 1
	if orderby is None:
		orderby = 'id'
	if resperpage is None:
		resperpage = 10
	l2 = libHtml()
	fields = ['firstname','lastname','team']
	go = get_object_or_404(Job,pk=int(job_id))
	o = Member.objects.filter(job=job_id).order_by(orderby)
	content = build_list_html(Member,o,fields,'job_list',[job_id,int(resperpage),int(bloc),orderby],'member_view')
	content = l2.section(go.title,content)
	content = l2.container(content,'div','col-md-8 col-md-offset-2')
	return render(request, 'gestion/template/form.html', locals())

def group_list(request,group_id,resperpage='10',bloc='1', orderby='id'):
	if bloc is None:
		bloc = 1
	if orderby is None:
		orderby = 'id'
	if resperpage is None:
		resperpage = 10
	l2 = libHtml()
	fields = ['firstname','lastname','job']
	o = Member.objects.filter(team=group_id).order_by(orderby)
	go = get_object_or_404(Team,pk=int(group_id))
	content = build_list_html(Member,o,fields,'group_list',[group_id,int(resperpage),int(bloc),orderby],'member_view')
	content = l2.section(go.title,content)
	content = l2.container(content,'div','col-md-8 col-md-offset-2')
	return render(request, 'gestion/template/form.html', locals())

def search(request):
	s = libHtml()
	content = s.input("text","recherche","","search")
	content += s.container("",'span',"","autocomplete")
	content = s.section("Recherche",content)
	content = s.container(content,'div','col-md-4 col-md-offset-4')
	return render(request, 'gestion/template/form.html', locals())

def ajax_member_list_delete(request):
	res = request.GET.get('res', None)
	res2 = res.split(',')
	val = ''
	for i in res2:
		o = get_object_or_404(Member, pk=int(i))
		val += '\t- ' + o.firstname + " " + o.lastname + '\n'
	print(val)
	data = {'val':val} 
	return JsonResponse(data)

def ajax_search(request):
	res = request.GET.get('term', None)
	res2 = res.split(' ')
	if res != None:
		s = libHtml()
		if len(res2) > 1:
			o = Member.objects.filter(Q(firstname__icontains=res) | 
			Q(lastname__icontains=res) |
			(Q(firstname__icontains=res2[0]) & Q(lastname__icontains=res2[1])) | 
			(Q(firstname__icontains=res2[1]) & Q(lastname__icontains=res2[0])))
		else:
			o=Member.objects.filter(Q(firstname__icontains=res) | Q(lastname__icontains=res))
		data = []
		for i in o:
			data1 = dict()
			data1['value'] = i.firstname + " " + i.lastname
			data1['label'] = "<a>" + s.photo_display(MEDIA_URL+str(i.photo),None,'32','32') + i.firstname + " " + i.lastname + "</a>"
			data1['url'] = reverse('member_view',args=[i.id])
			print(data1['label'])
			data.append(data1)
			print(data)
		return JsonResponse(data,safe=False)
	else:
		data = 'fail'
		mimetype = 'application/json'
		return HttpResponse(data, mimetype)