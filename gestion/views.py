from django.shortcuts import render, redirect,reverse,get_object_or_404
from django.db.models import Q
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from .forms import form_member_create, form_member_edit, form_job_create, form_team_create, form_login
from lib.form import lib_get_field_from_form
from lib.html import libHtml
from lib.list import build_list_html
from lib.model import get_verbose
from lib.javascript import libJava
from .models import Member,Job, Team
from lawapp.settings import MEDIA_URL,HOME_URL
from passlib.hash import pbkdf2_sha256
from .decorators import registered_user, redirect_on_connect

@registered_user
def member_create(request):
	"""
		Vue d'édition et de création des membres
	"""
	s = libHtml()
	form = form_member_create(request.POST or None,request.FILES) # Signifie que si le formulaire est retourné invalide il est rechargé avec les erreurs
	l = lib_get_field_from_form(form,Member)

	l1 = {1:{'Connection':
	[
		[[l["login"]["label"]],[l["login"]["field"]],
		[l["password"]["label"]],[l["password"]["field"]]]
	]},
	2:{'Identité':
	[
		[[l["firstname"]["label"]],[l["firstname"]["field"]],[l["lastname"]["label"]],[l["lastname"]["field"]]],
		[[l["photo"]["label"]],[l["photo"]["field"]]],
		[[l["team"]["label"]],[l["team"]["field"]]],
		[[l["job"]["label"]],[l["job"]["field"]]],
	]}
	}
	content = s.tab_with_fieldset(l1,'tab_form') 

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('member_list')		
		else:
			content = l['errors'] + s.tab_with_fieldset(l1,'tab_form')

	# content += s.fieldset('Identité',s.tableau(l2,None,False)) 
	content += s.tableau([[[s.submit_button("Envoyé")],[s.button("Liste des membres",reverse('member_list')),'class="right"']]],'tab_button')

	# Formation du formulaire
	content = s.form_cadre(request,"member_create",content,True)
	# content = l2.form_set_all(request,"create",form.as_table(),None,"azeazea")
	content = s.section('Création de membre',content,"stdsection")
	content = s.container(content,'div','col-md-6 col-md-offset-1')
		# Génération de la page en cas de réussite
	return render(request, 'gestion/template/form.html', locals())

@registered_user
def member_edit(request,member_id):
	obj = get_object_or_404(Member,pk=member_id)
	if request.method == 'POST':
		form = form_member_edit(request.POST or None,request.FILES,instance=obj) # Signifie que si le formulaire est retourné invalide il est rechargé avec les erreurs
	else:
		form = form_member_edit(instance=obj) # Instance = obj permet de préremplir
	l = lib_get_field_from_form(form,Member)
	s = libHtml()

	l1 = {1:{'Connection':
	[
		[[l["login"]["label"]],[l["login"]["field"]],["0"],["0"]]
	]},
		2:{'Identité':
	[
		[[l["firstname"]["label"]],[l["firstname"]["field"]],[l["lastname"]["label"]],[l["lastname"]["field"]]],
		[[l["photo"]["label"]],[l["photo"]["field"],'colspan=3']],
		[[l["team"]["label"]],[l["team"]["field"]]],
		[[l["job"]["label"]],[l["job"]["field"]]],
	]}
	}
	content = s.tab_with_fieldset(l1,'tab_form') 

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect(reverse('member_view',args=[member_id]))		
		else:
			content = l['errors'] + content

	# content += s.fieldset('Identité',s.tableau(l2,None,False)) 
	content += s.tableau([[[s.submit_button("Envoyé")],[s.button("Liste des membres",reverse('member_list')),'class="right"']]],'tab_button')

	# Formation du formulaire
	content = s.form_cadre(request,"member_edit",content,True,arg=[member_id])
	content = s.section('Edition de membre',content,'stdsection')
	content = s.container(content,'div','col-md-6 col-md-offset-1')

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
	content = build_list_html(request,Member,fields,'member_list',[int(resperpage),int(bloc),orderby],'member_view')
	content = l2.section('Liste des membres',content,'stdsection')
	content = l2.container(content,'div','col-md-8')
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

	content = l2.section(o.firstname + " " + o.lastname,l2.tableau(tabh,'wide',False),'stdsection')
	content = l2.container(content,'div','col-md-6 col-md-offset-1')
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
	content = l2.section('Création des profils',content,'stdsection')
	content = l2.container(content,'div','col-md-6 col-md-offset-1')
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
	content = l2.section('Création des équipes',content,'stdsection')
	content = l2.container(content,'div','col-md-6 col-md-offset-1')

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
	content = l2.section(go.title,content,'stdsection')
	content = l2.container(content,'div','col-md-8')
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
	content = l2.section(go.title,content,'stdsection')
	content = l2.container(content,'div','col-md-8')
	return render(request, 'gestion/template/form.html', locals())

def member_login(request):
	s = libHtml()
	form = form_login(request.POST or None)
	l = lib_get_field_from_form(form,Member)
	l1= [
	[[l["login"]["label"],'class="stdlab"'],[l["login"]["field"],'class="stdfield"']],
	[[l["password"]["label"]],[l["password"]["field"]]]
	]
	content = s.tableau(l1,'tab_form')
	content += s.submit_button("Envoyé")
	content = s.form_cadre(request,'member_login',content)
	if request.method == 'POST':
		if form.is_valid():
			Member.objects.get(login=form.cleaned_data['login']).connect(request)
			try: 
				url = request.session['current_url']
				del request.session['current_url']
				print(url)
				return redirect(url)
			except:
				return redirect(HOME_URL) 
		else:
			content = l["errors"] + content
	content = s.p("Vous devez être connecté pour acceder à cette page !")  + s.p("Veuillez vous connecter ...") + content
	content = s.section('Connection',content,'stdsection')
	content = s.container(content,'div','col-md-4 col-md-offset-2')
	return render(request, 'gestion/template/form.html', locals())


def member_logout(request):
	s = libHtml()
	j=libJava()
	request.session.flush()
	content = s.p("Votre session s'est bien terminée. A bientot !")
	content = s.section('Connection',content,'stdsection')
	content = s.container(content,'div','col-md-4 col-md-offset-2')
	content += j.redirect('member_list',"5000")
	return render(request, 'gestion/template/form.html', locals())

def search(request):
	s = libHtml()
	j = libJava()
	content = s.input("text","recherche","","search")
	content += s.container("",'span',"","autocomplete")
	content += j.autocomplete('search','autocomplete','/gestion/ajax_search/')
	content = s.section("Recherche",content,'stdsection')
	content = s.container(content,'div','col-md-4 col-md-offset-2')
	return render(request, 'gestion/template/form.html', locals())

def ajax_member_list_delete(request):
	res = request.GET.get('res', None)
	res2 = res.split(',')
	val = ''
	for i in res2:
		o = get_object_or_404(Member, pk=int(i))
		val += '\t- ' + o.firstname + " " + o.lastname + '\n'
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
			data.append(data1)
		return JsonResponse(data,safe=False)
	else:
		data = 'fail'
		mimetype = 'application/json'
		return HttpResponse(data, mimetype)

def ajax_member_connect(request):
	s= libHtml()
	login = request.GET.get('login', None)
	password = request.GET.get('password',None)
	try:
		o = Member.objects.get(login=login)
	except:
		o = None
	if o is not None and o.check_password(password):
		o.connect(request)
		data = {'url':'none'}
		for i in str(request.META['HTTP_REFERER']).split("/"):
			if i == 'member_login':
				try:
					url = request.session['current_url']
					del request.session['current_url']
				except:
					url = HOME_URL
				data = {'url':url}
	else:
		data = {"error" : s.p("Login et/ou mot de passe inconnu",idkey="c_connection_error")}
		
	return JsonResponse(data)	

def manage_quick_connect(obj=None):
	s = libHtml()
	if obj is not None:
		name = str(obj.firstname).capitalize() + " " + str(obj.lastname).upper()
		l = [
		[[s.photo_display(MEDIA_URL + str(obj.photo),None,"64"),'rowspan="2"'],[s.lien(name,reverse('member_view',args=[obj.id]))]],
		[[s.span(str(obj.job).capitalize(),classname="c_connected_job")]]
		]
		l = s.tableau(l,head=False)
		l2 = [
		[[l],[s.button(None,address=reverse('member_logout'),classname='danger left',glyph="off")]]
		]

		l = s.tableau(l2,head=False,table_class="c_connected")
	else:
		l= [
		[[s.input("text",None,"Login","c_login")]],
		[[s.input("password",None,"*****","c_password")]]
		]
		l = s.tableau(l,head=False)
		l2 = [
		[[l],[s.button("Ok",balise='button',classname='info',params='onClick="quick_connect()"')]]
		]
		l = s.container(s.tableau(l2,head=False,idkey="c_connection_table"),'div',None,"c_connection")
	return l
