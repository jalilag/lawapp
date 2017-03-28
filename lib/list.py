"""
	Librairie permettant la gestion et la génération de liste à partir des modeles
"""
from .html import libHtml
from .model import get_verbose
from django.urls import reverse
from lawapp.settings import MEDIA_URL

def build_list(class_model,fields,address_name,argx=[10,1,'id'], cell_link=None, head=True):
	"""
		Fonction de construction de liste à partir d'un modele
		res_num selectionne le nombre de résultat, si resnum = 0 on prend tout les resultats
		bloc_num permet le découpage en page, si il est sup au nbre de page possible la derniere page sera retournée
		head ajoute une première ligne titre avec les verboses names
		orderby permet de classer	
		arg = [...,res_num,bloc_num,orderby]
	""" 
	Narg = len(argx)
	orderby = argx[Narg-1]
	bloc_num = int(argx[Narg-2])
	res_num = int(argx[Narg-3])	
	print(orderby,bloc_num,res_num)
	slist = list()
	mainlist = list()
	l2 = libHtml()
	c = 0
	if orderby not in fields:
		orderby = fields[0]
	obj = class_model.objects.order_by(orderby)
	N = len(obj)
	if res_num > 0 and (int(N/res_num) < bloc_num-1):
		bloc_num = int(N/res_num)+1
	if head:
		for j in fields:
			arg = list(argx)
			arg[Narg-2]= '1'
			arg[Narg-3]= res_num
			if j == orderby:
				arg[Narg-1]= '-'+j
			else:
				arg[Narg-1]= j
			if j == 'delete':
				l1 = [l2.button(glyph="trash",classname="danger btn-xs del",buttype="button",balise="button",params='''onclick='check_del("''' + class_model.__name__ + '''","''' + class_model._meta.app_label + '''");\'''')]
				# l1 = ['<input id="button_delete" class="btn btn-danger btn-xs del" type="submit" value="X" />']
			else:
				l1 = [l2.lien(class_model._meta.get_field(j).verbose_name,reverse(address_name,args=arg))]
			slist.append(l1)
		mainlist.append(slist)
	for i in obj:
		c += 1
		if c>(bloc_num-1)*res_num and c<=bloc_num*res_num or res_num == 0:
			slist = list()
			for j in fields:
				if j == "photo":
					if cell_link is None:
						l1 = [l2.photo_display(MEDIA_URL+str(i.__getattribute__(j)))]
					else:
						l1 = [l2.photo_display(MEDIA_URL+str(i.__getattribute__(j))),
						"""onclick='location.href=\"""" + reverse(cell_link)+ """/"""+ str(i.__getattribute__('id')) + """\"'"""]
				elif j == "delete":
					l1 = [l2.checkbox('delete',i.__getattribute__('id'))]
				else:
					if cell_link is None:
						l1 = [i.__getattr__(j)]
					else:
						l1 = [i.__getattr__(j),"""onclick='location.href=\"""" + reverse(cell_link)+ """/"""+ str(i.__getattribute__('id')) + """\"'"""]						
				slist.append(l1)
			mainlist.append(slist)
	return mainlist

def build_list_html(request,class_model,fields,listaddress,argx=[10,1,'id'], cell_link=None, head=True):
	"""
		Fonction de mise en forme de liste a partir de modeles
		Affiche une liste avec tri possible
		Nombre de res
		Choix des pages
	"""
	Narg = len(argx)
	orderby = argx[Narg-1]
	bloc_num = argx[Narg-2]
	resperpage = argx[Narg-3]
	l2 = libHtml()
	# class_bsp = 'col-lg-6 col-lg-offset-3'
	# Boutons nombre de res
	res = ['5','10','20','50']
	but = '<table class="but_res"><tr>'
	for i in res:
		arg = list(argx)
		arg[Narg-3] = i
		but +='<td>'
		but += l2.button(i,reverse(listaddress,args=arg))
		but +='</td>'
	but += '</tr></table>'
	# Génération de la liste sous forme de tableau
	
	N = class_model.objects.count()
	l = l2.tableau(build_list(class_model,fields,listaddress,argx,cell_link,head),'class_list')
	content = but
	content += l
	# Génération des liens vers les pages
	content += res_per_page(listaddress,N,argx)
	if 'delete' in fields:
		content += l2.input('text',name="delete_address",val=listaddress,params='hidden=true')
		content += l2.input('text',name="delete_model",val=class_model.__name__,params='hidden=true')
		content += l2.input('text',name="delete_app",val=class_model._meta.app_label,params='hidden=true')
		content = l2.form_cadre(request,'ajax_list_delete_process',content,idkey='form_delete',name='form_delete')

	return content

def res_per_page(address_name,res_num,argx):
	"""
		Fonction permettant de générer une série de lien vers les pages de résultat
	"""
	Narg = len(argx)
	orderby = argx[Narg-1]
	currentpage = argx[Narg-2]
	resperpage = argx[Narg-3]
	# print(argx)
	l2 = libHtml()
	N = int(res_num/resperpage)+1
	if N > 1:
		content = 'Choisissez une page: '
		for i in range(currentpage-3,currentpage):
			if i > 0:
				arg = list(argx)
				arg[Narg-2] = str(i)
				content += l2.lien(str(i),reverse(address_name,args=arg))
				if i <= currentpage - 1:
					content += ', '
		content += l2.container(str(currentpage),'span','currentpage')
		if N > currentpage:
			content += ', '
		for i in range(currentpage+1,currentpage+4):
			if i <= N:
				arg = list(argx)
				arg[Narg-2] = str(i)
				content += l2.lien(str(i),reverse(address_name,args=arg))
				if i < currentpage+3 and i<N:
					content += ', '
		if i < N:
			content += ' ...'
	else:
		content =''
	return content


def list_of_one(key):
	while isinstance(key,list):
		key = key[0]
	return key
